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
            'name': ('Subcategory Two '),
        }


class SubcategoryTwo_Edit_Form(forms.ModelForm):
    class Meta:
        model = SubcategoryTwo
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': ('Subcategory Two '),
        }


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': ('Subcategory '),
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
        fields = ['name', 'subcategory','subcategory_two']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
            'subcategory_two': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': ('Name '),
            'subcategory': ('Subcategory'),
        }


class Category_Edit_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'subcategory','subcategory_two']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
            'subcategory_two': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': ('Name '),
            'subcategory': ('Subcategory'),
        }


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'reference', 'description', 'color', 'price', 'measured_type', 'area_total',
                  'image', 'environment', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'reference': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Reference'}),
            'description': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Description'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Color'}),
            'price': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Price'}),
            'measured_type': forms.Select(attrs={'class': 'form-control','placeholder': 'Measured Type'}),
            'area_total': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Area'}),
            'environment': forms.Select(attrs={'class': 'form-control','placeholder': 'Environment'}),
            'category': forms.Select(attrs={'class': 'form-control','placeholder': 'Category'}),
        }


class Material_Edit_Form(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'reference', 'description', 'color', 'price', 'measured_type', 'area_total',
                  'image', 'environment', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'reference': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Reference'}),
            'description': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Description'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Color'}),
            'price': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Price'}),
            'measured_type': forms.Select(attrs={'class': 'form-control','placeholder': 'Measured Type'}),
            'area_total': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Area'}),
            'environment': forms.Select(attrs={'class': 'form-control','placeholder': 'Environment'}),
            'category': forms.Select(attrs={'class': 'form-control','placeholder': 'Category'}),
        }


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['name', 'phone_number', 'email', 'address_company',
                  'activity', 'state', 'zip_code','material']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}),
            'address_company': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Address'}),
            'activity': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Activity'}),
            'state': forms.TextInput(attrs={'class': 'form-control','placeholder': 'State'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Zip Code'}),
            'material': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Material'}),
        }
        labels = {
            'name': ('Name'),
            'phone_number': ('Phone Number '),
            'email': ('Email'),
            'address_company': ('Address Company'),
            'activity': ('Activity'),
            'state': ('State'),
            'zip_code': ('Zip Code'),

        }


class Provider_Edit_Form(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['name', 'phone_number', 'email', 'address_company', 'activity',
                  'state', 'zip_code', 'material']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}),
            'address_company': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Address'}),
            'activity': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Activity'}),
            'state': forms.TextInput(attrs={'class': 'form-control','placeholder': 'State'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Zip Code'}),
            'material': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Material'}),

        }
        labels = {
            'name': ('Name'),
            'phone_number': ('Phone Number '),
            'email': ('Email'),
            'address_company': ('Address Company'),
            'activity': ('Activity'),
            'state': ('State'),
            'zip_code': ('Zip Code'),
            'contact': ('Contact'),
        }