from rest_framework import serializers
from .Models import Dish, Canteen, CReview, DReview, MyUser, DishState, Post
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework import status


class DishStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishState
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CanteenSerializer(serializers.Serializer):
    number = serializers.IntegerField()

    Canteen = ['work', 'dont work']
    status = serializers.ChoiceField(choices=Canteen)


def getDish():
    Dish = []
    Dish = list(Dish.objects.all().values('number').distinct())
    # print('\n\n\n', listDictDish, '\n\n\n')
    for dictDish in Dish:
        pkDish = dictDish['number']
        # print(type(numberDish))
        DishObject = Dish.objects.all().get(pk=pkDish)
        DishStateObjects = Dish.objects.all().filter(number=DishObject)
        Dish = Dish.order_by('-datetime')[0]
        serializer = Dish
        Dish.append(serializer.data)
    return Dish


def getCanteen():
    Canteen = []
    listDictCanteen = list(Canteen.objects.all().values('CanteenType').distinct())
    for dictCanteen in listDictCanteen:
        CanteenType = dictCanteen['CanteenType']
        CanteenObjects = Canteen.objects.all().filter(Canteen=CanteenType)
        Canteen = CanteenObjects.order_by('-datetime')[0]
        serializer = Canteen(Canteen)
        Canteen.append(serializer.data)
    return Canteen
