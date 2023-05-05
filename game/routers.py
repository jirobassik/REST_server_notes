from rest_framework import routers
from .views import GameViewSet
from genre.views import GameGenreViewSet
from game_platform.views import GamePlatformViewSet
from price.views import GamePriceViewSet

router = routers.SimpleRouter()
router.register(r'games', GameViewSet)
router.register(r'genre', GameGenreViewSet)
router.register(r'platform', GamePlatformViewSet)
router.register(r'price', GamePriceViewSet)
