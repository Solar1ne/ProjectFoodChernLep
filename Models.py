from django.db import models
from django.db import migrations
from django.contrib.auth.models import User



class Ingredient(models.Model):
    name = models.CharField(max_length=20)


class Dish(models.Model):
    name = models.CharField(max_length=20)
    additionDate = models.DateTimeField(auto_now_add=True, db_index=True)
    ingredients = models.ManyToManyField(Ingredient)


class Canteen(models.Model):
    name = models.CharField(max_length=20)
    additionDate = models.DateTimeField(auto_now_add=True, db_index=True)
    location = models.CharField(max_length=20)
    orating = models.IntegerField()
    trating = models.IntegerField()
    crating = models.IntegerField()
    qrating = models.IntegerField()
    dishes = models.ManyToManyField(Dish)
    description = models.TextField()

    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CReview(models.Model):
    canteen = models.ForeignKey(Canteen)
    orating = models.IntegerField()
    trating = models.IntegerField()
    crating = models.IntegerField()
    qrating = models.IntegerField()
    userName = models.CharField(max_length=15)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.userName


class DReview(models.Model):
    dish = models.ForeignKey(Dish)
    drating = models.IntegerField()
    userName = models.CharField(max_length=15)
    comment = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)


class MyUser(User):
    class Meta:
        ordering = ('username')

        proxy = True


class DishState(models.Model):
    datetime = models.DateTimeField(db_index=True)
    number = models.ForeignKey(Dish, verbose_name='Блюдо', on_delete=models.CASCADE)
    DISH_STATUS = ['FREE', 'BUSY', 'UNAVAILABLE']
    DISH_STATUS = ((status, status) for status in DISH_STATUS)
    status = models.CharField(verbose_name='Блюдо',  max_length=30)

    def __str__(self):
        return str(self.datetime) + ' | ' + str(self.number)


class Post(models.Model):
    comment = models.ForeignKey(DReview)
    text = models.TextField()
