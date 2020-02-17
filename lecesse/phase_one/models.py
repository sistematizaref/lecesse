from django.db import models

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
    description = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to='material')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    subcategory_two = models.ForeignKey(SubcategoryTwo, on_delete=models.CASCADE)
    type_measure = models.ForeignKey(TypeMeasure, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
