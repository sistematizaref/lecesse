from django.shortcuts import render, redirect
from phase_one.models import *
from phase_one.forms import SubcategoryForm,SubcategoryTwoForm, CategoryForm, Category_Edit_Form, MaterialForm, Material_Edit_Form, ProviderForm, Provider_Edit_Form

def home(request):
    """show phase one view"""
    materials = Material.objects.all()
    return render(request, 'index_phase_one.html',{'materials':materials})


def category(request):
    """show category view"""
    categories = Category.objects.all()
    if request.method == 'POST' and 'btnform1' in request.POST:
        form_subcategory = SubcategoryForm(request.POST)
        if form_subcategory.is_valid():
            data_subcategory = form_subcategory.save()
            return redirect('phase_one/category/')
        else:
            return render(request, 'category.html', {'form_subcategory': form_subcategory})
    if request.method == 'POST' and 'btnform2' in request.POST:
        form_subcategoryTwo = SubcategoryTwoForm(request.POST)
        if form_subcategoryTwo.is_valid():
            data_subcategory = form_subcategoryTwo.save()
            return redirect('phase_one/category/')
        else:
            return render(request, 'category.html', {'form_subcategoryTwo': form_subcategoryTwo})
    if request.method == 'POST' and 'btnform3' in request.POST:
        form_category = CategoryForm(request.POST)
        if form_category.is_valid():
            data_category = form_category.save()
            return redirect('phase_one/category/')
        else:
            return render(request, 'category.html', {'form_category': form_category})
    else:
        form_subcategory = SubcategoryForm()
        form_subcategoryTwo = SubcategoryTwoForm()
        form_category = CategoryForm()
        return render(request, 'category.html', {'form_subcategory': form_subcategory,
                                                'form_category': form_category,
                                                 'form_subcategoryTwo':form_subcategoryTwo,
                                                 'categories': categories})


def view_category(request, id_category):
    """can view data enviroment"""
    category = Category.objects.get(pk=id_category)
    return render(request, 'view_category.html', {'category': category})


def edit_category(request, id_category):
    """can edit a enviroment"""
    category = Category.objects.get(pk=id_category)

    if request.method == 'GET':
        # Get se usa para obtener datos y Post para enviar datos
        form = Category_Edit_Form(instance=category)
    else:
        # Aqui guardamos el cliente
        form = Category_Edit_Form(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('phase_one/category/')
    return render(request, 'edit_category.html', {'form': form})


def delete_category(request, id_category):
    """delete a category"""
    category = Category.objects.get(pk=id_category)
    category.delete()
    return redirect('phase_one/category/')


def materials(request):
    """show materials view"""
    materials = Material.objects.all()
    if request.method == 'POST':
        form_material = MaterialForm(request.POST, request.FILES)
        if form_material.is_valid():
            form_material.save()
            return redirect('phase_one/materials/')
        else:
            print("formulario no valido")
            print(form_material)
            return render(request, 'materials.html', {'form_material': form_material, 'materials':materials})
    else:
        form_material = MaterialForm()
        return render(request, 'materials.html', {'form_material': form_material, 'materials':materials})


def view_material(request, id_material):
    """can view data enviroment"""
    material = Material.objects.get(pk=id_material)
    return render(request, 'view_material.html', {'material': material})


def edit_material(request, id_material):
    """can edit a enviroment"""
    material = Material.objects.get(pk=id_material)

    if request.method == 'GET':
        # Get se usa para obtener datos y Post para enviar datos
        form = Material_Edit_Form(instance=material)
    else:
        # Aqui guardamos el cliente
        form = Material_Edit_Form(request.POST or None, request.FILES or None, instance=material)
        if form.is_valid():
            form.save()
            return redirect('phase_one/materials/')
    return render(request, 'edit_material.html', {'form': form})


def delete_material(request, id_material):
    """delete a category"""
    material = Material.objects.get(pk=id_material)
    material.delete()
    return redirect('phase_one/materials/')


def providers(request):
    """show providers view"""
    providers = Provider.objects.all()
    if request.method == 'POST':
        form_provider = ProviderForm(request.POST)
        if form_provider.is_valid():
            form_provider.save()
            return redirect('/phase_one/providers/')
        else:
            print("formulario no valido")
            print(form_provider)
            return render(request, 'providers.html', {'form_provider': form_provider, 'providers': providers})
    else:
        form_provider = ProviderForm()
        return render(request, 'providers.html', {'form_provider': form_provider, 'providers': providers})

def view_provider(request, id_provider):
    """can view data enviroment"""
    provider = Provider.objects.get(pk=id_provider)
    return render(request, 'view_provider.html', {'provider': provider})


def edit_provider(request, id_provider):
    """can edit a enviroment"""
    provider = Provider.objects.get(pk=id_provider)

    if request.method == 'GET':
        # Get se usa para obtener datos y Post para enviar datos
        form = Provider_Edit_Form(instance=provider)
    else:
        # Aqui guardamos el cliente
        form = Provider_Edit_Form(request.POST, instance=provider)
        if form.is_valid():
            form.save()
            return redirect('/phase_one/providers/')
    return render(request, 'edit_provider.html', {'form': form})


def delete_provider(request, id_provider):
    """delete a category"""
    provider = Provider.objects.get(pk=id_provider)
    provider.delete()
    return redirect('/phase_one/providers/')

