from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer  
from .models import Profile,User,Otp
from django.contrib.auth.password_validation import validate_password

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['password'] = user.password
        # ...

        return token
    


    def validate(self, attrs):
        data = super().validate(attrs)
        # Add any additional custom data here
        return data
    

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = 'first_name', 'last_name','username', 'email','password','password2','is_staff','is_active','is_admin'   

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
        
    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_staff=validated_data['is_staff'],
            is_active=validated_data['is_active'],
            is_admin=validated_data['is_admin'],    
            username=validated_data['username']

            )       
        

class ProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Profile
        fields = 'image','std','landline_no','fax','mobile_no','address','pincode','city','state','country'

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()  # Nested ProfileSerializer

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email','is_staff','is_active','date_joined','is_admin','created_at','user_permissions','profile' 

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)  # Extract profile data
        instance = super().update(instance, validated_data)

        if profile_data:
            # Update or create profile data if it exists
            Profile.objects.update_or_create(user=instance, defaults=profile_data)

        return instance 
   

class updatePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])    
    password2 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    otp = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        otp_status = Otp.objects.filter(user=attrs['otp']).exists()

        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
            return attrs

        elif otp_status == False:
            raise serializers.ValidationError({"otp": "Invalid OTP."})
        else:
            return attrs
    

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()

        return instance    

class loginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = User.objects.filter(email=attrs['email']).first()
        if user is None:
            raise serializers.ValidationError('User not found')
        return attrs
         

               
