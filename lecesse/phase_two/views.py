from django.shortcuts import render, redirect
from phase_two.models import *
from phase_two.forms import EnvironmentsForm, Environments_Edit_Form, Model_Apto_Form

# Create your views here.
def home(request):
    """show phase one view"""
    return render(request, 'index_phase_two.html')

def environment(request):
    """show phase one view"""
    environments = Environment.objects.all()
    if request.method == 'POST':
        form_environment = EnvironmentsForm(request.POST, request.FILES)
        if form_environment.is_valid():
            form_environment.save()
            return redirect('/phase_two/environments/')
        else:
            return render(request, 'environments.html', {'form_environment': form_environment, 'environments': environments})
    else:
        form_environment = EnvironmentsForm()
        return render(request, 'environments.html', {'form_environment': form_environment, 'environments': environments})

def edit_enviroment(request, id_enviroment):
    """can edit a enviroment"""
    enviroment = Environment.objects.get(pk=id_enviroment)

    if request.method == 'GET':
        # Get se usa para obtener datos y Post para enviar datos
        form = Environments_Edit_Form(instance=enviroment)
    else:
        # Aqui guardamos el cliente
        form = Environments_Edit_Form(request.POST, instance=enviroment)
        if form.is_valid():
            form.save()
            return redirect('/phase_two/environments/')
    return render(request, 'edit_environment.html', {'form': form})


def view_enviroment(request, id_enviroment):
    """can view data enviroment"""
    enviroment = Environment.objects.get(pk=id_enviroment)
    return render(request, 'view_environment.html', {'enviroment': enviroment})


def delete_enviroment(request, id_enviroment):
    """delete a enviroment"""
    enviroment = Environment.objects.get(pk=id_enviroment)
    enviroment.delete()
    return redirect('/phase_two/environments/')


def model_apartment(request):
    """show phase one view"""
    apartments = Apto_Model.objects.all()
    return render(request, 'model_apartment.html',{'apartments':apartments})

def create_apartment(request):
    """show phase one view"""
    if request.method == 'POST':
        form_apto = Model_Apto_Form(request.POST, request.FILES)
        if form_apto.is_valid():
            form_apto.save()
            return redirect('/phase_two/model_apartment/')
        else:
            return render(request, 'form_create_model_apto.html',
                          {'form_apto': form_apto})
    else:
        form_apto = Model_Apto_Form()
        return render(request, 'form_create_model_apto.html',
                      {'form_apto': form_apto})

def project(request):
    """show phase one view"""
    return render(request, 'project.html')
