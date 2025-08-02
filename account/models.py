from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, blank=False,null=False)
    phone_number = models.CharField(max_length=10,blank=False,null=False)
    email = models.EmailField(unique=True)
    is_manager = models.BooleanField(default=False)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username

