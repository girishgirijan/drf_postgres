from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CarsViewset(APIView):
    def get(self, request, id=None):
        if id:
            car = models.Cars.objects.get(id=id)
            serializer = serializers.CarsSerializer(car)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        cars = models.Cars.objects.all()
        serializer = serializers.CarsSerializer(cars, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.CarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        car = models.Cars.objects.get(id=id)
        serializer = serializers.CarsSerializer(
            car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        car = models.Cars.objects.filter(id=id)
        print(car)
        car.delete()
        return Response({"status": "success", "data": "Item deleted"})
