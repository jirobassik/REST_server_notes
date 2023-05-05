from rest_framework import viewsets
from .models import GamePriceModel
from .serializers import GenreSerializer


class GamePriceViewSet(viewsets.ModelViewSet):
    queryset = GamePriceModel.objects.all()
    serializer_class = GenreSerializer
