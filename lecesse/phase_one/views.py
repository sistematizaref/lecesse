from django.shortcuts import render, redirect
from phase_one.models import *
from phase_one.forms import SubcategoryForm

def home(request):
    """show phase one view"""
    return render(request, 'index_phase_one.html')


def category(request):
    """show category view"""
    return render(request, 'category.html')


def subcategory(request):
    """Create a subcategory"""
    print("entro a subcategory")
    subcategories = Subcategory.objects.all()
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data['name'])
            subcategory = Subcategory(
                name=data['name'],
            )
            subcategory.save()
            print("guardo la subcategoria")
            print(subcategory)
            return redirect('/phase_one/home/')
        else:
            return render(request, 'base_phase_one.html', {'form': form, 'subcategories': subcategories})
    else:
        form = SubcategoryForm()
        return render(request, 'base_phase_one.html', {'form': form, 'subcategories': subcategories})

def materials(request):
    """show materials view"""
    return render(request, 'materials.html')


def providers(request):
    """show providers view"""
    return render(request, 'providers.html')
