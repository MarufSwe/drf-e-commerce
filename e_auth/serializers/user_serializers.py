from django.db import transaction
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import Group

from e_auth.models import Profile
from e_auth.serializers.group_serializers import GroupDetailSerializer
from e_auth.serializers.profile_serializers import ProfileSerializerForUsers


class ProfileResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'image', 'gender', 'address', 'phone', 'father_name', 'mother_name', 'date_of_birth')


class UserLoginResponseSerializer(serializers.ModelSerializer):
    groups = GroupDetailSerializer(many=True)
    user_profile = ProfileResponseSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'groups', 'user_profile')


class UserDetailSerializer(serializers.ModelSerializer):
    groups = GroupDetailSerializer(many=True)
    user_profile = ProfileResponseSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        # fields = (
        #     'id', 'username', 'first_name', 'last_name', 'is_active', 'is_superuser', 'groups', 'user_permissions',
        #     'user_profile', 'user_nominee', 'user_job_records', 'user_training_details', 'user_academic_qualification',
        #     'user_emergency_contact',)


class UserListSerializer(serializers.ModelSerializer):
    user_profile = ProfileResponseSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'is_active', 'is_superuser', 'user_profile')


# User and Profile create together serializers
class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField(max_length=20, required=True)
    last_name = serializers.CharField(max_length=20, required=True)
    password = serializers.CharField(write_only=True)
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True)
    user_profile = ProfileSerializerForUsers()

    class Meta:
        model = User
        fields = (
            'id', 'username', 'password', 'first_name', 'last_name', 'is_active', 'is_superuser', 'groups',
            'user_profile')

    @transaction.atomic
    def create(self, validated_data):
        # Extract 'user_profile' data
        user_profile_data = validated_data.pop('user_profile')

        # Extract 'groups' data and remove it from validated_data
        groups_data = validated_data.pop('groups', [])

        # Create User instance without 'profile' and 'groups'
        user = User.objects.create_user(**validated_data)

        # Assign groups using set()
        user.groups.set(groups_data)

        # Create Profile instance and associate it with the user
        Profile.objects.create(user=user, **user_profile_data)

        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=20, required=True)
    last_name = serializers.CharField(max_length=20, required=True)
    user_profile = ProfileSerializerForUsers()

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True, 'required': False}}
        fields = (
            'id', 'username', 'password', 'first_name', 'last_name', 'is_active', 'is_superuser', 'groups',
            'user_permissions', 'user_profile')

    @transaction.atomic
    def update(self, instance, validated_data):
        user_profile_data = validated_data.pop('user_profile', {})

        # Update User instance fields
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        # Update User instance password if provided
        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        instance.save()

        # Update the associated profile
        user_profile, created = Profile.objects.get_or_create(user=instance)
        for attr, value in user_profile_data.items():
            setattr(user_profile, attr, value)
        user_profile.save()

        return instance
