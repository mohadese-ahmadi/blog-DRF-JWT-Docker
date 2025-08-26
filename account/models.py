from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Author(AbstractUser):
    sex_choices=[
        ('male','MALE'),
        ('female','FEMALE')]
    sex=models.CharField(choices=sex_choices, max_length=8)
    