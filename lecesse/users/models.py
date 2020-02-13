from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from users.choices import ROLE_CHOICES

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    document_number = models.CharField(max_length=150, null=False)
    phone_number = models.CharField(max_length=30, null=False)
    address = models.CharField(max_length=100, null=False)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, null=False)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []