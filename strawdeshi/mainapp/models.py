from django.db import models
from django.db import models  
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  
from django.utils import timezone  
from django.utils.translation import gettext_lazy as _  
from .managers import CustomUserManager  
# Create your models here.  
# Create your models here.
# class CustomUser(AbstractBaseUser, PermissionsMixin):  
# 	username = None  
# 	email = models.EmailField(_('email_address'), unique=True, max_length = 200)  
# 	date_joined = models.DateTimeField(default=timezone.now)  
# 	is_staff = models.BooleanField(default=False)  
# 	is_active = models.BooleanField(default=True)  
	  
  
  
# 	USERNAME_FIELD = 'email'  
# 	REQUIRED_FIELDS = []  
  
# 	objects = CustomUserManager()  
	  
# 	def has_perm(self, perm, obj=None):  
# 		"Does the user have a specific permission?"  
# 		# Simplest possible answer: Yes, always  
# 		return True  
  
# 	def is_staff(self):  
# 		"Is the user a member of staff?"  
# 		return self.staff  
  
# 	@property  
# 	def is_admin(self):  
# 		"Is the user a admin member?"  
# 		return self.admin  
  
# 	def __str__(self):  
# 		return self.email  


class Subscriber(models.Model):
    name=models.TextField(default="",null=True,blank=True)
    phone=models.TextField(default="",null=True,blank=True)
    email=models.EmailField(default="",null=True,blank=True)
    country=models.TextField(default="",null=True,blank=True)
    def __str__(self):
        return self.name+"_"+self.email+"_"+str(self.id)