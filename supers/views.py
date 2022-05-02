from ast import Delete
from urllib import request
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SupersSerializer
from .serializers import SupersSerializer
from .models import Supers
from .models import SuperTypes
from supers import serializers
from super_types import serializers

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        supertypes = request.query_params.get('type')
        supers = Supers.objects.all()
        if supertypes:
            supers = supers.filter(super_type__type=supertypes)
        serializer = SupersSerializer(supers, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SupersSerializer(supers)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SupersSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)