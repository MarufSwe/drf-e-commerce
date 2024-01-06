from django.db import transaction
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.conf import settings
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
# from django_filters.rest_framework import DjangoFilterBackend

import pytz
import datetime

# app
# from hrm_auth.filters.filters import UserFilter
from e_auth.paginations.paginations import CustomPageNumberPagination
# from hrm_auth.permissions.common_permissions import DjangoModelPermissionsWithGET
from e_auth.serializers.user_serializers import (
    UserCreateSerializer,
    UserListSerializer,
    UserDetailSerializer,
    UserUpdateSerializer,
    UserLoginResponseSerializer
)


# Login (POST): http://0.0.0.0:8000/api/login/

class Login(ObtainAuthToken):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        if response.status_code == status.HTTP_200_OK:
            # If authentication is successful, create or retrieve the user's token
            token, created = Token.objects.get_or_create(user=user)

            # Serialize the user data including 'first_name' and 'last_name'
            user_serializer = UserLoginResponseSerializer(user)

            # Add token-related and user data to the response
            response.data['token'] = token.key
            response.data.update(user_serializer.data)

        return response


# Logout (GET): http://0.0.0.0:8000/api/logout/
class Logout(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response({"message": "logout successful"}, status=status.HTTP_200_OK)


# Users http://0.0.0.0:8000/api/users/
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserDetailSerializer
    pagination_class = CustomPageNumberPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = UserListSerializer(page, many=True, context={"request": request})  # context = for image url
            return self.get_paginated_response(serializer.data)
        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = UserUpdateSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
