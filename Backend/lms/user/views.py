from django.shortcuts import render
from .models import User,Profile,Otp
from .serializers import UserSerializer,ProfileSerializer,RegisterSerializer,MyTokenObtainPairSerializer,loginSerializer, updatePasswordSerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets,generics
from rest_framework.permissions import AllowAny
import random
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import Http404
from django.core.mail import EmailMultiAlternatives
from rest_framework_simplejwt.views import TokenObtainPairView
from django.template.loader import render_to_string
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class ReactViewUserSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Define the queryset
    serializer_class = UserSerializer  # Define the serializer class


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
class ReactRegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer   

@api_view(['POST'])
def LoginView(request):
    # Using `request.data` to get the payload
    email = request.data.get('email')
    password = request.data.get('password')
    

    print("email:", email)
    print("password:", password)
    
    # Implement your login logic here
    serializer_class = loginSerializer
    serializer = serializer_class(data=request.data)
    if serializer.is_valid():
        user = User.objects.filter(email=email).first()
        print("Login successful")
        token = MyTokenObtainPairSerializer.get_token(user)
        print("token: ", token)
        return Response({
            "token":  str(token),
            "fullname": str(user.get_full_name()),
            "email": str(user.email),
                          
        }, status=200)
    else:
        return Response(serializer.errors, status=400)

    

 

 # def post(self, request, *args, **kwargs):
    #     email = request.data.get('email')
    #     password = request.data.get('password')

       

        



    # def post(self, request, *args, **kwargs):
        # serializer = self.get_serializer(data=request.data)
        # if serializer.is_valid():
        #         # Handle login logic here
        #         print("Login successful")
        #         return Response({"message": "Login successful"}) 
        


class ReactViewUserDetails(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def get_object(self):
        email = self.kwargs.get('email')
        user = User.objects.filter(email=email).first()
        return user
             

class PasswordResetEmailVerifyAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    
    def get_object(self):
        email = self.kwargs.get('email')
        user = User.objects.filter(email=email).first()

        if user is not None:
                uuidb64 = user.pk
                refresh = RefreshToken.for_user(user)
                refresh_token = str(refresh.access_token)
                otp = Otp.objects.create(user=user)
                otp.generate_otp()
                otp.refresh_token = refresh_token
                otp.save()
                 
                link = f'http://localhost:3020/reset-password/?otp={otp.otp}&uuidb64={uuidb64}&=refresh_token={refresh_token}'
   
        return user
          
class PasswordChangeAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = updatePasswordSerializer

    def create(self, request, *args, **kwargs):
        uuidb64 = request.data.get('uuidb64')   
        otp = request.data.get('otp')
        password = request.data.get('password')
        user = User.objects.filter(pk=uuidb64).first()

        if user is not None:
            otp_obj = Otp.objects.filter(user=user).first()
            if otp_obj is not None:
                if otp_obj.otp == otp:
                    user.set_password(request.data.get('new_password'))
                    user.save()
                    return Response({'detail': 'Password changed successfully.'}, status=200)
                else:
                    return Response({'detail': 'Invalid OTP.'}, status=400)
            else:
                return Response({'detail': 'OTP expired.'}, status=400)
        else:    
            return Response({'detail': 'User not found.'}, status=404)  


 