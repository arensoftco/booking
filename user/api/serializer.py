from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from ..models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email_address', 'address', 'is_employee', 'is_admin', 'profile_picture', 'created_at', 'updated_at']
        extra_kwargs = {
            'password':{'write_only':True},
            'is_employee':{'required':False},
            'is_admin':{'required':False},
        }

    def validate_email_address(self, value):
        try:
            validate_email(value)
            return value
        except ValidationError:
            raise serializers.ValidationError('Geçerli bir E-Posta adresi giriniz.')

    def create(self, validated_data):
        user = CustomUser(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            
        )
        return super().create(validated_data)