from rest_framework import serializers

from .models import Cat, Owner


# сериализатор для модели Cat
class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cat
        fields = ('id', 'name', 'color', 'birth_year')


# сериализатор для модели Owner
class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = ('first_name', 'last_name')
