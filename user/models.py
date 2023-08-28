from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    username = PhoneNumberField(unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank = False, null = False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email_address = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    address = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True, blank=False, null=False)
    is_employee = models.BooleanField(default=False, blank=False)
    is_admin = models.BooleanField(default=False, blank=False)

    profile_picture = models.ImageField(upload_to='profile_photos', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)