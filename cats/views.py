# импортируем пакет viewsets
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cat, Owner
from .serializers import CatSerializer, OwnerSerializer


# создаем вьюсет - наследник самого распространенного класса-вьюсета
# ModelViewSet
# этот класс-вьюсет может выполнять любые операции CRUD с моделью
# не нужно указывать методы, нужно только указать два обязательных поля
# выборка объектов модели, с которой будет работать вьюсет
# и сериализатор, который будет применяться
class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    # Пишем метод, а в декораторе разрешим работу со списком объектов
    # и переопределим URL на более презентабельный
    @action(detail=False, url_path='recent-white-cats')
    def recent_white_cats(self, request):
        # Нужны только последние пять котиков белого цвета
        cats = Cat.objects.filter(color='белый')[:5]
        # Передадим queryset cats сериализатору
        # и разрешим работу со списком объектов
        serializer = self.get_serializer(cats, many=True)
        return Response(serializer.data)


# создаем вьюсет - наследник самого распространенного класса-вьюсета
# ModelViewSet
# этот класс-вьюсет может выполнять любые операции CRUD с моделью
# не нужно указывать методы, нужно только указать два обязательных поля
# выборка объектов модели, с которой будет работать вьюсет
# и сериализатор, который будет применяться
class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
