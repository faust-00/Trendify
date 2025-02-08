from rest_framework import serializers
from user.models import User


class UserUpdateSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=False)  # optional bo'lishi mumkin
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'address', 'phone_number', 'date_of_birth', 'full_name']
