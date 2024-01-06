from rest_framework import serializers
from e_auth.models import Profile


class ProfileSerializerForUsers(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('image', 'gender', 'phone', 'father_name', 'mother_name', 'address', 'date_of_birth',)
