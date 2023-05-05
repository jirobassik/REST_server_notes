from rest_framework import serializers
from .models import GamePriceModel


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePriceModel
        fields = ('id', 'name', 'price', "price_currency", 'game')
