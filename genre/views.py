from rest_framework import viewsets
from .models import GameGenreModel
from .serializers import GenreSerializer


class GameGenreViewSet(viewsets.ModelViewSet):
    queryset = GameGenreModel.objects.all()
    serializer_class = GenreSerializer
