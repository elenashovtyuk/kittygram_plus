from django.urls import include, path
# импортируем необходимый роутер
from rest_framework.routers import DefaultRouter
# импортируем нужные вьюсеты
from cats.views import CatViewSet, LightCatViewSet, OwnerViewSet

# создаем экземпляр роутера
router = DefaultRouter()
# регистрируем эндпоинты, т.е
# создаем необходимый набор эндпоинтов
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
router.register(r'mycats', LightCatViewSet)
# после регистрации включаем новые эндпоинты
# в список urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
