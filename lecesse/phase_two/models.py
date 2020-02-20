from django.db import models
from phase_two.choices import *


class Environment(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=150, null=False)
    measured_type = models.CharField(max_length=100, null=False, choices=MEASURED_TYPE)
    area_total = models.CharField(max_length=150, null=False)
    icon = models.ImageField(upload_to='environment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Apto_Model(models.Model):
    name = models.CharField(max_length=100, null=False)
    identifier = models.CharField(max_length=150, null=False)
    flat = models.ImageField(upload_to='model_apto')
    cover_page = models.ImageField(upload_to='model_apto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name_project = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=150, null=False)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    zip_code = models.CharField(max_length=150, null=False)
    owner_project = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
