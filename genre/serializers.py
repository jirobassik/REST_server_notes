from rest_framework import serializers
from .models import GameGenreModel


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameGenreModel
        fields = '__all__'
