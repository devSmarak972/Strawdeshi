from django.contrib import admin

# Register your models here.
from django.contrib.auth import authenticate  
from django.contrib.auth.admin import UserAdmin  
# from mainapp.models import CustomUser
from mainapp.models import *
from mainapp.managers import CustomUserManager
# from mainapp.forms import CustomUserChangeForm,CustomUserCreationForm
# # Register your models here.  
# class CustomUserAdmin(UserAdmin):  
#     add_form = CustomUserCreationForm  
#     form = CustomUserChangeForm  
#     model = CustomUser  
  
#     list_display = ('email', 'is_staff', 'is_active',)  
#     list_filter = ('email', 'is_staff', 'is_active',)  
#     fieldsets = (  
#         (None, {'fields': ('email', 'password')}),  
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),  
#     )  
#     add_fieldsets = (  
#         (None, {  
#             'classes': ('wide',),  
#             'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}  
#         ),  
#     )  
#     search_fields = ('email',)  
#     ordering = ('email',)  
#     filter_horizontal = ()  
  
admin.site.register(Subscriber)