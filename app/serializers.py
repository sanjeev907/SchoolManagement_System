from rest_framework import serializers 
from .models import *


class schoolSerializer(serializers.Serializer):
    email=serializers.CharField(required=True, error_messages={"error_message":"email is required"})
    name=serializers.CharField(required=True, error_messages={"error_message":"name is required"})
    city=serializers.CharField(required=True, error_messages={"error_message":"city is required"})
    pincode=serializers.IntegerField(required=True, error_messages={"error_message":"pincode is required"})
    password=serializers.CharField(required=True, error_messages={"error_message":"password is required"})


class studentsSerializer(serializers.Serializer):
    name=serializers.CharField(required=True, error_messages={"error_message":"name is required"})
    grade=serializers.CharField(required=True, error_messages={"error_message":"name is required"})
    username=serializers.CharField(required=True, error_messages={"error_message":"name is required"})
    password=serializers.CharField(required=True, error_messages={"error_message":"name is required"})


class schoolLoginSerializer(serializers.Serializer):
    email=serializers.CharField(required=True, error_messages={"error_message":"name is required"})
    password=serializers.CharField(required=True, error_messages={"error_message":"name is required"})
    

   