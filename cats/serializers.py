import datetime as dt
# import webcolors
from rest_framework import serializers

# импортируем нужные для работы модели
from .models import Cat, Owner, Achievement, AchievementCat


# сериализатор для модели Achievement
class AchievementSerializer(serializers.ModelSerializer):
    achievement_name = serializers.CharField(source='name')

    class Meta:
        model = Achievement
        fields = ('id', 'achievement_name')


# # опишем новый тип поля Hex2NameColor
# class Hex2NameColor(serializers.Field):
#     # при чтении данных ничего не меняем -
#     # просто возвращаем как есть
#     def to_representation(self, value):
#         return value
#     # при записи код цвета конвертируется в его название
#     def to_internal_value(self, data):
#         # проверяем
#         try:
#             # если имя цвета существует, то конвертируем код в название
#             data = webcolors.hex_to_name(data)
#         except ValueError:
#             # иначе возвращаем ошибку
#             raise serializers.ValidationError('Для этого цвета нет имени')
#         # возвращаем данные в новом формате
#         return data


# сериализатор для модели Cat
class CatSerializer(serializers.ModelSerializer):

    # Убираем owner = serializers.StringRelatedField(read_only=True)
    # переопределяем поле achievements.
    # Теперь это поле будет получать объекты Achievement,
    # сериализованные в AchievementSerializer
    # достижений у котика может быть много, поэтому добавляем аттрибут
    # many=True
    # кроме того, так как поле achievements не должно быть обязательным
    # нужно явно его переопределить - указать аттрибут required=False
    achievements = AchievementSerializer(many=True, required=False)
    # добавим новое поле в сериалайзер (его нет в модели)
    age = serializers.SerializerMethodField()
    # после создания класса Hex2NameColor можем добавитть
    # это новое пользовательское поле в CatSerializer
    # таким образом переопределяем поле color
    # color = Hex2NameColor()

    class Meta:
        model = Cat
        fields = ('id', 'name', 'color', 'birth_year', 'owner', 'achievements', 'age')

    # чтобы настроить сохранение данных, нужно переопределить метод create()
    # в сериализаторе
    # validated_data - это словарь с проверенными данными, полученными
    # в результате POST-запроса
    def get_age(self, obj):
        return dt.datetime.now().year - obj.birth_year

    def create(self, validated_data):
        # проверим - пришло в запросе поле achievement или нет
        # и в зависимости от результата будем сохранять котика
        # с достижениями или без
        # если такого поля нет, то создаем запись о котике без его достижений

        if 'achievements' not in self.initial_data:
            cat = Cat.objects.create(**validated_data)
            return cat

        # иначе делаем следующее:

        # уберем список достижений из списка serializer.validated_data
        # и сохраним его в переменную achivement
        achievements = validated_data.pop('achievements')

        # дальше создаем нового котика пока без достижений
        # **validated_data - распаковка словаря
        cat = Cat.objects.create(**validated_data)

        # для каждого достижения из списка достижений
        for achievement in achievements:
            # создадим новую запись(новое достижение) или получим
            # существующий экземпляр из БД
            # (существующее достижение котов)
            current_achievement, status = Achievement.objects.get_or_create(
                **achievement)
            AchievementCat.objects.create(
                achievement=current_achievement, cat=cat)
        return cat


# сериализатор для модели Owner
class OwnerSerializer(serializers.ModelSerializer):
    cats = serializers.StringRelatedField(many=True, read_only=True)
# сериализаторы могут работать со связанными моделями
# для этого укажем related_name cats в списке полей сериализатора

    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'cats')
