from rest_framework import viewsets
from .models import GameModel
from .serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = GameModel.objects.all()
    serializer_class = GameSerializer
