from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Drink
from core.serializers import DrinkSerializer


@api_view(['GET', 'POST'])
def drinks(request):
    if request.method == 'GET':
        # get all drinks, serialize them and return them
        all_drinks = Drink.objects.all()
        serializer = DrinkSerializer(all_drinks, many=True) # this returns a list of all the drinks as JSON list of
        # dictionaries.
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def drink_by_id(request, drink_id):
    try:
        drink = Drink.objects.get(pk=drink_id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

