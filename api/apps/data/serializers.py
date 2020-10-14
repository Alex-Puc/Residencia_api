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

class CoachSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coach
        fields = [
            'user',
            'sport',
            'created_at',
            'updated_at'
        ]

class SportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sport
        fields = [
            'name',
            'descript',
            'training',
            'created_at',
            'updated_at'
        ]

class TrainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Training
        fields = [
            'name',
            'descript',
            'repetition',
            'duration',
            'created_at',
            'updated_at'
        ]


