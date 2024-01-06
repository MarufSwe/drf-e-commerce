from django.db import models
from django.contrib.auth.models import User


# Profile Table
class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE = 'ML', 'Male'
        FEMALE = 'FL', 'Female'

    # each user will be a single profile
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    image = models.ImageField(upload_to='images', null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True, null=True, choices=Gender.choices, default=Gender.MALE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    father_name = models.CharField(max_length=50, null=True, blank=True)
    mother_name = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    date_of_birth = models.DateField(editable=True, null=True, blank=True)
