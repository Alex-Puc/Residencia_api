from rest_framework import serializers
from .models import Athlete, Coach, Training, Sport

class AthleteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    sport = serializers.StringRelatedField()

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
    user = serializers.StringRelatedField()
    sport = serializers.StringRelatedField()

    class Meta:
        model = Coach
        fields = [
            'user',
            'sport',
            'created_at',
            'updated_at'
        ]

class SportSerializer(serializers.ModelSerializer):
    training = serializers.StringRelatedField(many=True)

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
    exercise = serializers.StringRelatedField(many=True)
    day = serializers.StringRelatedField(many=True)

    class Meta:
        model = Training
        fields = [
            'name',
            'descript',
            'exercise',
            'day',
            'created_at',
            'updated_at'
        ]


