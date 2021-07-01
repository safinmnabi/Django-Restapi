from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username','email', 'password' )

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ('id','fullname','email','mobile','message','userid')
