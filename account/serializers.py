# Serializers

from rest_framework import serializers
from account.models import User

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        depth = 0
        fields = ['id', 'username', 'introduction', 'lang', 'solved', 'submit_time', 'email', 'is_staff', 'is_superuser', 'date_joined', 'is_active']
        read_only_fields = ['id', 'email', 'solved', 'submit_time']
