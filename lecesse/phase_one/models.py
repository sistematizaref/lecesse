from django.db import models
from phase_one.choices import *

class SubcategoryTwo(models.Model):
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, null=False)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    subcategory_two = models.ForeignKey(SubcategoryTwo, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TypeMeasure(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100, null=False)
    reference = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200, null=False)
    color = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100, null=False)
    measured_type = models.CharField(max_length=100, null=False, choices=MEASURED_TYPE)
    area_total = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to='material')
    environment = models.CharField(max_length=100, null=False, choices=ENVIRONMENTS)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Contact(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    position = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=100, null=False)
    responsible_account = models.CharField(max_length=100, null=False)
    project_name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class Provider(models.Model):
    name = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    address_company = models.CharField(max_length=200, null=False)
    activity = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    zip_code = models.CharField(max_length=100, null=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

