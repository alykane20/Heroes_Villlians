from rest_framework import serializers
from .models import Power, Super

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name', 'alter_ego', 'powers', 'catchphrase', 'super_type_id', 'super_type']
        depth = 1
    super_type_id = serializers.IntegerField(write_only=True)

class PowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power
        fields = ['id', 'name']

    