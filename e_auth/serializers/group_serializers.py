from rest_framework import serializers
from django.contrib.auth.models import Group
from e_auth.serializers.permission_serializers import PermissionSerializer


class GroupDetailSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')


class GroupSerializerForUserList(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')