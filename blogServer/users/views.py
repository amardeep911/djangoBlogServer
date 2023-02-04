from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from users.serializer import UserRegistrationSerializer
from users.serializer import UserLoginSerializer
from django.contrib.auth import authenticate
from users.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from users.serializer import UserProfileSerializer
# Create your views here.
#Generate Token manually

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistratiionView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token,'msg': 'registration successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    # def post(self,request, format=None):
    #     # data = request.data
    #     # serializer = UserLoginSerializer(data=data)
    #     # if serializer.is_valid():
    #     return Response('good', status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        
        print(request.data)
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg': 'Log in Screen'}, status=status.HTTP_200_OK)
            else:
                return Response({'msg': 'password or username not matched'})
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)