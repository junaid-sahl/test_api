from rest_framework import serializers

from authentication.models import UserAccount


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'
