from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from .models import User, Otp
import random
from django.shortcuts import get_object_or_404


# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


'''class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        if not request.data.get('phone_number'):
            return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)
        user = get_object_or_404(User, phone_number=request.data.get('phone_number'))
        code=random.randint(1000,9999)
        otp = Otp.objects.create(user=user, otp=code,phone_number=user.phone_number)
        name= user.username if user.username else  'Your verification code is {}'.format(code)
        to_phone_number = user.phone_number
        message = f'Hello {name},\n this is your confidential verification code: {code}.\nPlease do not share it with anyone.'
        print(message)

        #Email sending code goes here

        request.session['otp'] = code
        request.session['user'] = user.username
        return Response({'message': 'Verification code sent successfully'}, status=status.HTTP_200_OK)'''
