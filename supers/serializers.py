from rest_framework import serializers
from .models import SuperTypes

class SupersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        field = ('name', 'alter_ego', 'primary ability', 'secondary ability', 'catchphrase', 'super type')