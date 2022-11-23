from django.urls import include, path
from rest_framework.authtoken import views
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
    path('api-token-auth/', views.obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
