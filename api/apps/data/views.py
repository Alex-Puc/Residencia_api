from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView,  DestroyAPIView

from .serializers import AthleteSerializer, CoachSerializer, SportSerializer, TrainingSerializer, ExerciseSerializer

from rest_framework import filters as df

from .models import Athlete, Coach, Sport, Training, Exercise
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



#Coach

class CoachListView(ListAPIView):
    serializer_class = CoachSerializer
    permission_classes = ()
    queryset = Coach.objects.all()
    filter_backends = (df.OrderingFilter, df.SearchFilter, )
    search_fields = ('user_name', )
    ordering_fields = ('name',)

#metodo POST
class CoachCreateView(CreateAPIView):
    serializer_class = CoachSerializer
    permission_classes = ()

#metodo get 'id'
class CoachRetrieveView(RetrieveAPIView):
    serializer_class = CoachSerializer
    permission_classes = ()
    queryset = Coach.objects.all()
    lookup_field = 'id'

#metodo Put/Patch
class CoachUpdateView(UpdateAPIView):
    serializer_class = CoachSerializer
    permission_classes = ()
    queryset = Coach.objects.all()
    lookup_field = 'id'

#metodo Delete
class CoachDestroyView(DestroyAPIView):
    permission_classes = ()
    queryset =Coach.objects.all()
    lookup_field = 'id'



#sport
class SportListView(ListAPIView):
    serializer_class = SportSerializer
    permission_classes = ()
    queryset = Sport.objects.all()
    filter_backends = (df.OrderingFilter, df.SearchFilter, )
    search_fields = ('name', )
    ordering_fields = ('name',)

#metodo POST
class SportCreateView(CreateAPIView):
    serializer_class = SportSerializer
    permission_classes = ()

#metodo get 'id'
class SportRetrieveView(RetrieveAPIView):
    serializer_class = SportSerializer
    permission_classes = ()
    queryset = Sport.objects.all()
    lookup_field = 'id'

#metodo Put/Patch
class SportUpdateView(UpdateAPIView):
    serializer_class = SportSerializer
    permission_classes = ()
    queryset = Sport.objects.all()
    lookup_field = 'id'

#metodo Delete
class SportDestroyView(DestroyAPIView):
    permission_classes = ()
    queryset = Sport.objects.all()
    lookup_field = 'id'



#training
class TrainingListView(ListAPIView):
    serializer_class = TrainingSerializer
    permission_classes = ()
    queryset = Training.objects.all()
    filter_backends = (df.OrderingFilter, df.SearchFilter, )
    search_fields = ('name', )
    ordering_fields = ('name',)

#metodo POST
class TrainingCreateView(CreateAPIView):
    serializer_class = TrainingSerializer
    permission_classes = ()

#metodo get 'id'
class TrainingRetrieveView(RetrieveAPIView):
    serializer_class = TrainingSerializer
    permission_classes = ()
    queryset = Training.objects.all()
    lookup_field = 'id'

#metodo Put/Patch
class TrainingUpdateView(UpdateAPIView):
    serializer_class = TrainingSerializer
    permission_classes = ()
    queryset = Training.objects.all()
    lookup_field = 'id'

#metodo Delete
class TrainingDestroyView(DestroyAPIView):
    permission_classes = ()
    queryset = Training.objects.all()
    lookup_field = 'id'


#exercise
class ExerciseListView(ListAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = ()
    queryset = Exercise.objects.all()
    filter_backends = (df.OrderingFilter, df.SearchFilter, )
    search_fields = ('name', )
    ordering_fields = ('name',)

#metodo POST
class ExerciseCreateView(CreateAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = ()

#metodo get 'id'
class ExerciseRetrieveView(RetrieveAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = ()
    queryset = Exercise.objects.all()
    lookup_field = 'id'

#metodo Put/Patch
class ExerciseUpdateView(UpdateAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = ()
    queryset = Exercise.objects.all()
    lookup_field = 'id'

#metodo Delete
class ExerciseDestroyView(DestroyAPIView):
    permission_classes = ()
    queryset = Exercise.objects.all()
    lookup_field = 'id'