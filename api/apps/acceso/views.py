import json
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import Response, APIView
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework import exceptions, permissions,generics

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from jwt.exceptions import InvalidSignatureError
import jwt

from common.pagination import PageNumberPagination

from . import serializers
from . import forms
from . import utils
from . import models
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.


class Me(APIView):
    def get(self, request):
        user = request.user
        serializer = serializers.UserDetailSerializer(user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserUpdate(generics.RetrieveUpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserDetailSerializer

class RegisterView(CreateAPIView):
    permission_classes = ()

    from django.views.decorators.debug import sensitive_post_parameters
    from django.utils.decorators import method_decorator
    sensitive_post_parameters_m = method_decorator(
        sensitive_post_parameters('password', 'password_confirm')
    )
    serializer_class = serializers.RegisterSerializer

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)

    def get_response_data(self, user):
        from django.utils.six import text_type
        refresh = RefreshToken.for_user(user)
        cxt = {
            'refresh': text_type(refresh),
            'access': text_type(refresh.access_token)
        }
        # print('response data', cxt)
        return cxt


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        # Send mail confirmation
        # user.send_confirmation_mail()
        return user


class UsersView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        # Start pagination instance class
        paginator = PageNumberPagination()
        objects = models.User.objects.filter(
            type__in=[1,2,3,4],
            is_active=True,
            is_staff=False
        )
        # Result page
        result_page = paginator.paginate_queryset(objects, request)
        # Serialize objects
        serializer = serializers.UserDetailSerializer(result_page, many=True,context={'request': request})

        return paginator.get_paginated_response(serializer.data)

    def put(self, request, pk):
        user = models.User.objects.get(pk=pk)
        serializer = serializers.UserDetailSerializer(
            user, data=request.data,context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            password = request.data.get('password', None)
            if password:
                user.set_password(request.data.get('password'))
                user.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = models.User.objects.get(pk=pk)
        user.is_active = False
        user.save()
        return Response(None, 204)


class ResetPasswordView(APIView):
    permission_classes = ()

    def put(self, request):
        serializer = serializers.ResetPasswordSerializer(
            data=request.data
        )
        if serializer.is_valid():
            user = utils.get_user_by_code(code=request.data.get('code'))
            # Set value reminder
            user.set_password(request.data.get('password'))
            user.reminder = None
            user.save()

            return Response({'success': 'ok'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def reset_password(request, user_id, token):
    user = get_object_or_404(models.User, pk=user_id)
    if request.method == 'POST':
        form = forms.ResetPasswordForm(request.POST)

        try:
            jwt.decode(token, user.password, algorithms='HS256')
        except InvalidSignatureError:
            form = forms.ResetPasswordForm()
            messages.error(request, 'El link para cambiar contraseña ya no es válido.')
            return render(request, 'email/reset_password.html', {'form': form})

        if form.is_valid():
            new_password = form.cleaned_data.get('password')
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Contraseña actualizada de forma correcta.')
            return render(request, 'email/reset_password.html', {'form': form})
    else:
        form = forms.ResetPasswordForm(initial={'token': token})

    return render(request, 'email/reset_password.html', {'form': form})

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.MyTokenObtainPairSerializer


class RecoverPasswordView(APIView):
    permission_classes = ()

    def post(self, request):

        email = request.data.get('email', None)

        user = utils.user_by_email(email=email)
        if not user:
            raise exceptions.ValidationError('Not exist email {}'.format(
                email
            ))

        # Send sms validation
        from common import utils as cutils
        from django.conf import settings
        
        token = jwt.encode({'user_id': user.pk}, user.password, algorithm='HS256').decode('utf-8')

        link = '{}/v1/reset-password/{}/{}/'.format(
            settings.URL_WEBSITE,
            user.id,
            token
        )
        subject = 'Recuperar contraseña'
        cutils.send_mail(
            recipient=[user.email],
            subject=subject,
            template='email/recover-password.html',
            context={
                    'display_name': user.display_name(),
                    'site': settings.APPNAME,
                    'link': link
            }
        )

        return Response({'success': 'ok'}, status=status.HTTP_200_OK)