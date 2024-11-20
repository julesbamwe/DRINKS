"""
    This is used to change python objects into json objects or Data.
"""
from rest_framework import serializers
from core.models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink  # This is the class that has objects that have to be changed into json.
        fields = ['id', 'name', 'description']  # These are the fields that have to be sent back
