from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from .serializers import UsuarioSerializer




@api_view(['POST'])
def login_view(request):

    user=get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({'error': 'Contraseña incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created=Token.objects.get_or_create(user=user)
    serializer=UsuarioSerializer(instance=user)

    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def register_view(request):
    serializer = UsuarioSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user=User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()

        token=Token.objects.create(user=user)
        return Response({'token': token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)


    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile_view(request):
    user = request.user
    print(request.user.password)
    serializer = UsuarioSerializer(instance=user)
    return Response(serializer.data, status=status.HTTP_200_OK)