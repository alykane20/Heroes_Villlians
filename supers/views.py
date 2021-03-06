from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Power, Super
from super_types.models import Super_type


@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        custom_response_dictionary = {}
        type_param = request.query_params.get('type')
        supers = Super.objects.all()
        if type_param:
            supers = supers.filter(super_type__type = type_param)
            serializer = SuperSerializer(supers, many=True)
            return Response(serializer.data)
        else:
            super_types = Super_type.objects.all()
            for type in super_types:
                supers = Super.objects.filter(super_type_id=type.id)
                serializer = SuperSerializer(supers, many=True)
                custom_response_dictionary[type.type] = {
                "Supers": serializer.data 
            }
        return Response(custom_response_dictionary)
    
    elif request.method =='POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
def super_power(request, pk, power_type):
    if request.method == 'PATCH':
        super = get_object_or_404(Super, pk=pk)
        power = get_object_or_404(Power, name=power_type)
        super.powers.add(power)
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    
    
