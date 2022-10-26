from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,username,first_name,last_name,mobile,email,password=None):
        if not email:
            raise ValueError('you must have an email address')
        user = self.model(
            email = self.normalize_email(email),
            username=username,
            first_name = first_name,
            last_name=last_name,
            mobile=mobile,
            password=password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

         
  
    def create_superuser(self,username,first_name,last_name,email,mobile,password):
        user=self.create_user(
            email = self.normalize_email(email),
            username= username,
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name      = models.CharField(max_length=50)
    last_name      = models.CharField(max_length=50)
    username        =models.CharField(max_length=50)
    email           =models.EmailField(max_length=100,unique=True)   
    mobile          =models.CharField(max_length=10,unique=True,null=True)
    password        =models.CharField(max_length=220,blank=False,null=False)
    qualification = models.CharField(max_length=220,blank=False,null=False)
    dp              =models.ImageField(upload_to='photos/users_dp/',blank=True)
    bio             =models.TextField(blank=True,null=True)
    interests       =models.TextField(max_length=1000,null=True,blank=True)
    wallet_balance  =models.IntegerField(default=0)
    account_holder_name =models.CharField(max_length=200,null=True,blank=True)
    bank            =models.CharField(max_length=200,null=True,blank=True)
    acc             =models.CharField(max_length=20,null=True,blank=True)
    ifsc            =models.CharField(max_length=20,null=True,blank=True)
    courses_created =models.IntegerField(default=0)
    courses_enrolled=models.IntegerField(default=0)
    
    
    joined_date     =models.DateTimeField(auto_now_add=True)
    last_login      =models.DateTimeField(auto_now=True)
    is_staff        =models.BooleanField(default=False)
    is_active       =models.BooleanField(default=False)
    is_verified     =models.BooleanField(default=False)
    is_superuser   =models.BooleanField(default=False)
    is_admin   =models.BooleanField(default=False)

    USERNAME_FIELD  ='email'
    REQUIRED_FIELDS =['password','username','first_name','last_name','mobile']
    
    objects=MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True


class UserToken(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()