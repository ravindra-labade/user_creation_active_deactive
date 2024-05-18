from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    username = serializers.EmailField()
    otp = serializers.CharField( write_only=True )
    class Meta:
        model = User
        fields = ['username', 'password', 'otp']


    def create(self, validated_data):
        validated_data.pop('otp')
        return User.objects.create_user(**validated_data)
