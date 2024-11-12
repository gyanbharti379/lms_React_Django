from datetime import datetime, timezone

from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.db import models
from django.templatetags.static import static
import random


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True) 
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField(unique=True) 
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='media/images/user.png', upload_to='profile_pics')
    std = models.CharField(max_length=5)
    landline_no = models.IntegerField(unique=True, default="111111111")
    fax = models.IntegerField(default="1234567890")
    mobile_no = models.IntegerField(default="1234567890")
    address = models.TextField(max_length=100)
    pincode = models.IntegerField(default="111111")
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
   
    def __str__(self):
            return self.user.get_full_name()
           

class LoginAttempts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    failed_login_count = models.IntegerField(default=0)
    success_login_count = models.IntegerField(default=0)
    
    def __str__(self):  
        return self.user.get_full_name()

    def get_failed_login_count(self):
        return self.failed_login_count
     
    def increment_failed_login_count(self):
        self.failed_login_count += 1
        self.save()

    def increment_success_login_count(self):
        self.success_login_count += 1   
        self.save() 

    def get_success_login_count(self):
        return self.success_login_count 
    

class Otp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6, null=True, blank=True)
    refresh_token = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()
    
    def generate_otp(self):
        self.otp = str(random.randint(100000, 999999))
        self.save() 
    
    def get_otp(self):
        return self.otp
  
            

