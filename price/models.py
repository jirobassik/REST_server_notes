from django.db import models
from game.models import GameModel
from djmoney.models.fields import MoneyField

class GamePriceModel(models.Model):
    name = models.CharField("Название магазина", max_length=40, null=False, blank=False, db_index=True)
    price = MoneyField("Цена", max_digits=10, decimal_places=2, default_currency="USD")
    game = models.ForeignKey(GameModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
