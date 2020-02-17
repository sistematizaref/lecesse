from django import forms
from phase_one.models import *

class SubcategoryTwoForm(forms.ModelForm):
    class Meta:
        model = SubcategoryTwo
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': ('Name '),
        }


class SubcategoryTwo_Edit_Form(forms.ModelForm):
    class Meta:
        model = SubcategoryTwo
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': ('Name '),
        }


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': ('Name '),
        }


class Subcategory_Edit_Form(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': ('Name '),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'subcategory']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': ('Name '),
            'subcategory': ('Subcategory'),
        }


class Category_Edit_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'subcategory']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': ('Name '),
            'subcategory': ('Subcategory'),
        }