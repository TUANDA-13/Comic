from asyncio.windows_events import NULL
from tkinter.tix import Tree
from django.db import models
import os
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
# Create your models here.

class Profile(models.Model):
    
    GENDER_CHOICES = (
        ("Boy", "Boy"),
        ("Girl", "Girl"),
        ("Other", "Other"),
    )
    
    def update_filename(instance, filename):
        path = "img/profile"
        format = str(instance.id)+'.'+ filename.split('.')[-1]
        return os.path.join(path, format)
    
    Name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    Phone = models.CharField(validators=[phone_regex], max_length=10) # Validators should be a list
    Gender = models.CharField(choices=GENDER_CHOICES,default=GENDER_CHOICES[0],max_length=20)
    Avatar = models.ImageField(blank=True,upload_to=update_filename, height_field=None, width_field=None, max_length=100,null=True)
    Account = models.OneToOneField("Account",on_delete=models.CASCADE,blank=True,null=True,related_name='profile')
    
    def __str__(self) -> str:
        return str(self.id)

class Account (models.Model):
    def update_filename(instance, filename):
        path = "img/account"
        format = str(instance.id)+'.'+ filename.split('.')[-1]
        return os.path.join(path, format)
    # Profile = models.OneToOneField("Profile",on_delete=models.CASCADE,blank=True,null=True,related_name='account')
    Password = models.CharField(max_length=50)
    Email = models.EmailField()

    def __str__(self) -> str:
        return str(self.id)

