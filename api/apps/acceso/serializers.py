from rest_framework import serializers, exceptions

from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from common.utils import get_thumbnail_image
from .adapters import DefaultAccountAdapter
from . import utils

User = get_user_model()

def get_adapter():
    return DefaultAccountAdapter()

class UserDetailSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField(read_only=True) 
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'photo',
            'type',
            'media'
        ]

    def get_media(self, instance):
        if instance.photo:
            #'http://localhost:8000'+
            return get_thumbnail_image(self.context.get('request'),instance.photo.url)
        else:
            return None

class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True, max_length=30)
    last_name = serializers.CharField(required=True, max_length=30)
    type = serializers.ChoiceField(required=True, choices=User.USER_TYPE)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        # if allauth_settings.UNIQUE_EMAIL:
        if True:
            # if email and email_address_exists(email):
            if email and User.objects.filter(email=email).exists():
                raise serializers.ValidationError(
                    "A user is already registered with this e-mail address.")
        return email

    def validate_password(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        password1 = data.get('password')
        password2 = data.get('password_confirm')
        # user_type = data.get('type')
        if password1 != password2:
            raise serializers.ValidationError("The two password fields didn't match.")
        return data

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('email'),
            'password': self.validated_data.get('password_confirm', ''),
            'email': self.validated_data.get('email', ''),
            'type': self.validated_data.get('type', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        }

    def custom_signup(self, request, user):
        pass

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'password_confirm',
            'type',
        ]

class ResetPasswordSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    password = serializers.CharField(required=True, style={
        'input_type': 'password'
    })
    password_confirm = serializers.CharField(required=True, style={
        'input_type': 'password'
    })

    def validate_code(self, code):
        user = utils.get_user_by_code(code=code)

        if not user:
            msg = 'Not exist code'
            raise exceptions.ValidationError(msg)

        return user

    def validate(self, data):
        password = data.get('password')
        password_confirm = data.get('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError(
                "The two password fields didn't match."
            )

        return data

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['display_name'] = user.display_name()
        # print(token)
        # ...

        return token

