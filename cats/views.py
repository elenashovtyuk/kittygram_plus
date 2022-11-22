# импортируем пакет viewsets
from rest_framework import viewsets

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


# создаем вьюсет - наследник самого распространенного класса-вьюсета
# ModelViewSet
# этот класс-вьюсет может выполнять любые операции CRUD с моделью
# не нужно указывать методы, нужно только указать два обязательных поля
# выборка объектов модели, с которой будет работать вьюсет
# и сериализатор, который будет применяться
class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
