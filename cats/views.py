# импортируем пакет viewsets
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cat, Owner
from .serializers import CatSerializer, CatListSerializer, OwnerSerializer


# создаем свой базовый вьюсет с особым набором действий
# унаследуем его от миксинов с нужными действиями и дполнительно
# от базового класса GenericViewSet
# в итоге получаем базовый вьюсет, который будет создавать объект и
# получать экземпляр объекта
# теперь от этого класса можно унаследоваться
class CreateRetrieveViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    pass


# опишем новый вьюсет, унаследованный от созданного ранее базового вьюсета
class LightCatViewSet(CreateRetrieveViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer()

# создаем вьюсет - наследник самого распространенного класса-вьюсета
# ModelViewSet
# этот класс-вьюсет может выполнять любые операции CRUD с моделью
# не нужно указывать методы, нужно только указать два обязательных поля
# выборка объектов модели, с которой будет работать вьюсет
# и сериализатор, который будет применяться


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    # стандартный метод, который позволяет определить, какой
    # из доступных сериализаторов должен обрабатывать данные
    # если запрошенное действие(action)- получение списка объектов

    def get_serializer_class(self):
        if self.action == 'list':
            # то применяем CatListSerializer
            return CatListSerializer
        # если запрошенное действие не 'list',
        # то применяем CatSerializer
        return CatSerializer
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
