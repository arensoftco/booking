from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from PIL import Image
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError(_('The Phone Number must be set'))
        
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_super_user=True'))
        return self.create_superuser(phone_number, password, **extra_fields)
        

class CustomUser(AbstractUser):
    username = None
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager

    def __str__(self):
        return self.phone_number

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    address = models.TextField(blank=True)
    job_start_date = models.DateField(null=True, blank=True)
    email_address = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='profile_photos')
    active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} {self.first_name} {self.last_name}'
    
    def save(self, *args, **kwargs):
        ## IMAGE RESIZE
        super().save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            if img.height > 600 or img.width > 600:
                output_size = (600,600)
                img.thumbnail(output_size)
                img.save(self.photo.path)


class Employee_Rating(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='ratings')
    commentator = models.CharField(max_length=200)
    comment = models.TextField(blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    rating = models.PositiveBigIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f'{self.rating} {self.employee}'

 
class Employee_Working_Day_Time(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='working_days_times')
    day_number = models.SmallIntegerField()
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.employee}, {self.day_number}, {self.start_time}, {self.end_time}'


""" class Employee_Appointment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name = 'services')
    employee = models.ForeignKey(Employee, on_delete=models.SET(1), related_name='employees')
    appointment_time = models.DateTimeField()
    duration = models.SmallIntegerField()
    description = models.TextField(blank=True, null=True)
    color_code = models.CharField(max_length=7)
    done = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{Service.service_name}, {Employee.first_name} {Employee.last_name}, {self.appointment_time}' """