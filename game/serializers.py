from rest_framework import serializers
from .models import GameModel
from genre.serializers import GenreSerializer
from genre.models import GameGenreModel
from game_platform.serializers import GamePlatformSerializer
from game_platform.models import GamePlatformModel

class GameSerializer(serializers.ModelSerializer):
    # genres = GenreSerializer(many=True, read_only=False, queryset=GameGenreModel.objects.all())
    # game_platform = GamePlatformSerializer(many=True, read_only=False, queryset=GamePlatformModel.objects.all())

    class Meta:
        model = GameModel
        fields = '__all__'


