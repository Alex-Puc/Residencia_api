from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView,  DestroyAPIView

from .serializers import AthleteSerializer

from rest_framework import filters as df

from .models import Athlete
from apps.acceso.models import User

# Create your views here.


#metodo Get
class AthleteListView(ListAPIView):
    serializer_class = AthleteSerializer
    permission_classes = ()
    queryset = Athlete.objects.all()
    filter_backends = (df.OrderingFilter, df.SearchFilter, )
    search_fields = ('hit', )
    ordering_fields = ('hit',)

#metodo POST
class AthleteCreateView(CreateAPIView):
    serializer_class = AthleteSerializer
    permission_classes = ()

#metodo get 'id'
class AthleteRetrieveView(RetrieveAPIView):
    serializer_class = AthleteSerializer
    permission_classes = ()
    queryset = Athlete.objects.all()
    lookup_field = 'id'

#metodo Put/Patch
class AthleteUpdateView(UpdateAPIView):
    serializer_class = AthleteSerializer
    permission_classes = ()
    queryset = Athlete.objects.all()
    lookup_field = 'id'

#metodo Delete
class AthleteDestroyView(DestroyAPIView):
    permission_classes = ()
    queryset = Athlete.objects.all()
    lookup_field = 'id'

