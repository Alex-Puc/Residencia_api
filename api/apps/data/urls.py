from rest_framework import routers
from . import views
from django.urls import path

router = routers.DefaultRouter()

urlpatterns = [
    path('athletes/', views.AthleteListView.as_view(), name = 'athletes'),
    path('athletes/create/', views.AthleteCreateView.as_view(), name = 'athlete_create'),
    path('athletes/<int:id>/', views.AthleteRetrieveView.as_view(), name = 'athlete'),
    path('athletes/<int:id>/update/', views.AthleteUpdateView.as_view(), name='athlete_update'),
    path('athletes/<int:id>/delete/', views.AthleteDestroyView.as_view(), name='athlete_delete'),

    path('coachs/', views.CoachListView.as_view(), name = 'coachs'),
    path('coachs/create/', views.CoachCreateView.as_view(), name = 'coach_create'),
    path('coachs/<int:id>/', views.CoachRetrieveView.as_view(), name = 'coach'),
    path('coachs/<int:id>/update/', views.CoachUpdateView.as_view(), name='coach_update'),
    path('coachs/<int:id>/delete/', views.CoachDestroyView.as_view(), name='coach_delete'),

    path('sports/', views.SportListView.as_view(), name = 'sports'),
    path('sports/create/', views.SportCreateView.as_view(), name = 'sport_create'),
    path('sports/<int:id>/', views.SportRetrieveView.as_view(), name = 'sport'),
    path('sports/<int:id>/update/', views.SportUpdateView.as_view(), name='sport_update'),
    path('sports/<int:id>/delete/', views.SportDestroyView.as_view(), name='sport_delete'),

    path('trainings/', views.TrainingListView.as_view(), name = 'trainings'),
    path('trainings/create/', views.TrainingCreateView.as_view(), name = 'training_create'),
    path('trainings/<int:id>/', views.TrainingRetrieveView.as_view(), name = 'training'),
    path('trainings/<int:id>/update/', views.TrainingUpdateView.as_view(), name='training_update'),
    path('trainings/<int:id>/delete/', views.TrainingDestroyView.as_view(), name='training_delete'),

    path('exercises/', views.ExerciseListView.as_view(), name = 'exercise'),
    path('exercises/create/', views.ExerciseCreateView.as_view(), name = 'exercise_create'),
    path('exercises/<int:id>/', views.ExerciseRetrieveView.as_view(), name = 'exercise'),
    path('exercises/<int:id>/update/', views.ExerciseUpdateView.as_view(), name='exercise_update'),
    path('exercises/<int:id>/delete/', views.ExerciseDestroyView.as_view(), name='exercise_delete'),

]

urlpatterns += router.urls


