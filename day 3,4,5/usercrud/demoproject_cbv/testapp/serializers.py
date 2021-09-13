from rest_framework import serializers
from django.contrib.auth.models import User

def username_length(value):
    if len(value) < 8:
        raise serializers.ValidationError("username must contain atleast 8 char")

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, validators= [username_length,]) 
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

    def validate_email(self, value):
        l1 = value.split('@')
        s1 = 'gmail.com'
        if s1 not in l1:
            raise serializers.ValidationError('domain name must be gmail.com')
        return value



