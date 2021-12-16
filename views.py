from django.db import migrations
from rest_framework import generics, status, serializers
from rest_framework.response import Response
from django.db import models
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse, JsonResponse
from .Models import Canteen, Dish, DishState, Post
from .serializers import Dish, CanteenSerializer, getDish, getCanteen, DishStateSerializer, PostSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView

ONLINE = True


@api_view(['GET'])
def api_dish(request, pk):
    if request.method == 'GET':
        if ONLINE :
            state = DishState.objects.get(pk=pk)
            serializer = DishStateSerializer(instance=state)
            return Response(serializer.data)
        else:
            return Response(None, status=status.HTTP_503_SERVICE_UNAVAILABLE)


@api_view(['GET'])
def api_Canteen(request):
    if request.method == 'GET':
        if ONLINE :
            qs = Canteen.objects.all()
            serializer = CanteenSerializer(instance=qs, many=True)
            return Response(serializer.data)
        else:
            return Response(None, status=status.HTTP_503_SERVICE_UNAVAILABLE)



class Home(APIView):
    def get(request):
        return Response("<h1>Main page</hq>")


class Contact(APIView):
    def get(request):
        return Response("<h1>asdasdasdasd page</hq>")


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #
    # def create(self, request, *args, **kwargs):
    #     super(PostCreateView, self).create(request, args, kwargs)
    #     response = {"status_code": status.HTTP_200_OK,
    #                 "message": "Successfully created",
    #                 "result": request.data}
    #     return Response(response)

