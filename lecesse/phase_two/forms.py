from django import forms
from .models import *

class EnvironmentsForm(forms.ModelForm):
    class Meta:
        model = Environment
        fields = ['name', 'description','measured_type','area_total','icon']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Description'}),
            'measured_type': forms.Select(attrs={'class': 'form-control','placeholder': 'Measured Type'}),
            'area_total': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Area'})
        }
        labels = {
            'name': ('Name '),
            'description': ('Description'),
            'area_total': ('Area'),
        }


class Environments_Edit_Form(forms.ModelForm):
    class Meta:
        model = Environment
        fields = ['name', 'description', 'measured_type', 'area_total', 'icon']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'measured_type': forms.Select(attrs={'class': 'form-control'}),
            'area_total': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'name': ('Name '),
            'description': ('Description'),
            'area_total': ('Area'),
        }


class Model_Apto_Form_First(forms.ModelForm):
    class Meta:
        model = Apto_Model
        fields = ['name', 'identifier','flat','cover_page']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'identifier': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Identifier'}),
        }
        labels = {
            'name': ('Name '),
            'description': ('Description')
        }



class Edit_Model_Apto_Form(forms.ModelForm):
    class Meta:
        model = Apto_Model
        fields = ['name', 'identifier','flat','cover_page']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'identifier': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Identifier'}),
        }
        labels = {
            'name': ('Name '),
            'description': ('Description')
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name_project','address','city','state','zip_code',
                  'owner_project', 'utility']
        widgets = {
            'name_project': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_project': forms.TextInput(attrs={'class': 'form-control'}),
            'utility': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name_project': ('Name'),
            'address': ('Address'),
            'city': ('City'),
            'state': ('State'),
            'zip_code': ('Zip Code'),
            'owner_project': ('Owner Project'),
            'utility': ('Utility')
        }


class Project_Edit_Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name_project', 'address', 'city', 'state', 'zip_code',
                  'owner_project']
        widgets = {
            'name_project': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_project': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name_project': ('Name'),
            'address': ('Address'),
            'city': ('City'),
            'state': ('State'),
            'zip_code': ('Zip Code'),
            'owner_project': ('Owner Project'),
        }

class Contact_Form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_number', 'position', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Phone Number'}),
            'position': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Position'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email'}),
        }

class Building_Form(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['number_builings', 'number_floors']
        widgets = {
            'number_builings': forms.TextInput(attrs={'class': 'form-control'}),
            'number_floors': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Various_Form(forms.ModelForm):
    class Meta:
        model = various
        fields = ['type_measure', 'area', 'price', 'provider']
        widgets = {
            'type_measure': forms.Select(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'provider': forms.Select(attrs={'class': 'form-control'}),
        }