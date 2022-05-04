from rest_framework import serializers
from .models import Supers

class SupersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ('name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type')
        depth = 1 

class SupersPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ('name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type')
        
        