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
]

urlpatterns += router.urls


