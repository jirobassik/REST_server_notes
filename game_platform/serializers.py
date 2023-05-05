from rest_framework import serializers
from .models import GamePlatformModel
from rest_framework.relations import PrimaryKeyRelatedField

class GamePlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePlatformModel
        fields = '__all__'
