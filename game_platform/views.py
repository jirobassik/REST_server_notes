from rest_framework import viewsets
from .models import GamePlatformModel
from .serializers import GamePlatformSerializer


class GamePlatformViewSet(viewsets.ModelViewSet):
    queryset = GamePlatformModel.objects.all()
    serializer_class = GamePlatformSerializer
