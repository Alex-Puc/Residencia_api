from rest_framework import serializers
from .models import Athlete, Coach, Training, Sport

class AthleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Athlete
        fields = [
            'user',
            'sport',
            'hit',
            'weigth',
            'muscle'
        ]



