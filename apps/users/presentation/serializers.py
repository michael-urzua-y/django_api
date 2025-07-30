from rest_framework import serializers
from apps.users.domain.user_model import User
from apps.users.domain.commerce_model import Commerce

class CommerceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commerce
        fields = [
            'commerce_id',
            'name',
            'document',
            'document_format',
            'iso_code',
            'created_at',
            'updated_at',
            'deleted_at'
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id',
            'commerce_id', 
            'name',
            'email',
            'password',
            'ip',
            'role',
            'permissions',
            'position',
            'is_active',
            'created_at',
            'updated_at',
            'deleted_at'
        ]

