from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import UserValidationSerializer, UserCreateSerializer
from rest_framework.views import APIView


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

# @api_view(['POST'])
# def registration(request):
#     serializer = UserCreateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     User.objects.create_user(**serializer.validated_data)
#     return Response(status=status.HTTP_201_CREATED)


class AuthorizationAPIView(APIView):
    def post(self, request):
        serializer = UserValidationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_403_FORBIDDEN)

# @api_view(['POST'])
# def authorization(request):
#     serializer = UserValidationSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = authenticate(**serializer.validated_data)
#     if user is not None:
#         token, _ = Token.objects.get_or_create(user=user)
#         # try:
#         #     token = Token.objects.get(user=user)
#         # except Token.DoesNotExist:
#         #     token = Token.objects.create(user=user)
#         return Response(data={'key': token.key})
#     return Response(status=status.HTTP_403_FORBIDDEN)
