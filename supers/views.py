from ast import Delete
from urllib import request
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SupersSerializer
from .models import Supers
from supers import serializers

@api_view(['GET','POST'])
def supers_list(request):
    if request.method == 'GET':
        super_type = request.query_params.get('type')
        queryset = Supers.objects.all()
        if super_type:
            queryset = queryset.filter(super_type__type = super_type)
        serializer = SupersSerializer(queryset, many =True) 
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)