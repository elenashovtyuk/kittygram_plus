from django.db import models


CHOICES = (
        ('Gray', 'Серый'),
        ('Black', 'Чёрный'),
        ('White', 'Белый'),
        ('Ginger', 'Рыжий'),
        ('Mixed', 'Смешанный'),
    )

# cоздаем модель, которая хранит информацию о достижениях кота
class Achievement(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


# создаем класс, в котором будет храниться информация
# о хозяинах котов
class Owner(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# создаем класс, в котором будет храниться информация
# о котах
class Cat(models.Model):
    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16, choices=CHOICES)
    birth_year = models.IntegerField()
    # добавим новое поле, которое будет связывть
    # модель Cat с моделью Owner
    owner = models.ForeignKey(
        Owner, related_name='cats', on_delete=models.CASCADE)
    # также добавим поле,
    # которое будет связывать модель Cat с моделью Achievement
    # через вспомогательную модель AchievementCat
    achievements = models.ManyToManyField(
        Achievement, through='AchievementCat')

    def __str__(self):
        return self.name


# создаем новый класс Achivments
# в котором будет связаны id котика и id его достижения
# это промежуточная модель для обеспечения связи
# между моделями Cat и Achievement
class AchievementCat(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.achievement} {self.cat}'
