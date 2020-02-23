from django.db import models
from phase_two.choices import *
from phase_one.models import *


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
    name = models.CharField(max_length=100, null=True)
    identifier = models.CharField(max_length=150, null=True)
    flat = models.ImageField(upload_to='model_apto')
    cover_page = models.ImageField(upload_to='model_apto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class various(models.Model):
    type_measure = models.CharField(max_length=100, null=True,  choices=MEASURED_TYPE)
    area = models.CharField(max_length=150, null=True)
    price = models.CharField(max_length=150, null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
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
    utility = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_project


class Contact(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=100, null=False)
    position = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True,max_length=40)
    id_project = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.first_name

class Building(models.Model):
    number_builings = models.CharField(max_length=100, null=False)
    number_floors = models.CharField(max_length=100, null=False)
    id_project = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.number_builings

