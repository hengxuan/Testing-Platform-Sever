from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.password = make_password(validated_data.get('password', instance.password))
        instance.save()
        return instance
