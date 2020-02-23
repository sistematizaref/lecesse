from django.shortcuts import render, redirect
from phase_two.models import *
from phase_two.forms import EnvironmentsForm, Environments_Edit_Form, \
    Model_Apto_Form_First, Project_Edit_Form, \
    ProjectForm, Edit_Model_Apto_Form, Contact_Form, Building_Form, Various_Form
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
    """show phase one view"""
    projects = Project.objects.all()
    return render(request, 'index_phase_two.html',{'projects':projects})

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def view_enviroment(request, id_enviroment):
    """can view data enviroment"""
    enviroment = Environment.objects.get(pk=id_enviroment)
    return render(request, 'view_environment.html', {'enviroment': enviroment})

@login_required(login_url='/login/')
def delete_enviroment(request, id_enviroment):
    """delete a enviroment"""
    enviroment = Environment.objects.get(pk=id_enviroment)
    enviroment.delete()
    return redirect('/phase_two/environments/')

@login_required(login_url='/login/')
def model_apartment(request):
    """show phase one view"""
    apartments = Apto_Model.objects.all()
    return render(request, 'model_apartment.html',{'apartments':apartments})


@login_required(login_url='/login/')
def create_apartment(request):
    """show phase one view"""
    environments = Environment.objects.all()
    if request.method == 'POST':
        form_apto = Model_Apto_Form_First(request.POST, request.FILES)
        if form_apto.is_valid():
            form_apto.save()
            print("entro")
            return render(request, 'form_create_model_apto_two.html',
                          {'environments':environments})
        else:
            print("no valido")
            return render(request, 'form_create_model_apto.html',
                          {'form_apto': form_apto})
    else:
        form_apto = Model_Apto_Form_First()
        return render(request, 'form_create_model_apto.html',
                      {'form_apto': form_apto})


@login_required(login_url='/login/')
def create_apartment_tree(request):
    """show phase one view"""
    environments = Material.objects.all()
    form = Various_Form()
    return render(request, 'form_create_model_apto_tree.html', {'form': form, 'environments':environments})

@login_required(login_url='/login/')
def create_apartment_finish(request):
    """show phase one view"""
    return render(request, 'finish_model_apto.html')

@login_required(login_url='/login/')
def edit_apartment(request, id_apartment):
    """can edit a enviroment"""
    apartment = Apto_Model.objects.get(pk=id_apartment)

    if request.method == 'GET':
        # Get se usa para obtener datos y Post para enviar datos
        form = Edit_Model_Apto_Form(instance=apartment)
    else:
        # Aqui guardamos el cliente
        form = Edit_Model_Apto_Form(request.POST, instance=apartment)
        if form.is_valid():
            form.save()
            return redirect('/phase_two/model_apartment/')
    return render(request, 'edit_apartment.html', {'form': form})

@login_required(login_url='/login/')
def view_apartment(request, id_apartment):
    """can view data enviroment"""
    apartment = Apto_Model.objects.get(pk=id_apartment)
    return render(request, 'view_apartment.html', {'apartment': apartment})

@login_required(login_url='/login/')
def delete_apartment(request, id_apartment):
    """delete a enviroment"""
    apartment = Apto_Model.objects.get(pk=id_apartment)
    apartment.delete()
    return redirect('/phase_two/model_apartment/')


@login_required(login_url='/login/')
def project(request):
    """show phase one view"""
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})


@login_required(login_url='/login/')
def create_pro(request):
    """create a project"""
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            request.session['id_project'] = project.id
            return redirect('/phase_two/create_cont/')
        else:
            return render(request, 'create_project.html', {'form': form})
    else:
        form = ProjectForm()
        return render(request, 'create_project.html', {'form': form})


@login_required(login_url='/login/')
def create_cont(request):
    """can view data enviroment"""
    contacts = Contact.objects.all()
    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print("guardo")
            id_project = request.session.get('id_project')
            contact = Contact(
                first_name=data['first_name'],
                last_name=data['last_name'],
                phone_number=data['phone_number'],
                position=data['position'],
                email=data['email'],
                id_project=id_project
            )
            contact.save()
            return redirect('/phase_two/create_cont/')
        else:
            print("No valido form")
            return render(request, 'create_contact.html', {'form_contact': form})
    else:
        form_contact = Contact_Form()
        print("Entro a crear cont")
        return render(request, 'create_contact.html', {'form_contact': form_contact, 'contacts': contacts })



@login_required(login_url='/login/')
def view_pro(request, id_project):
    """can view data enviroment"""
    project = Project.objects.get(pk=id_project)
    return render(request, 'view_project.html', {'project': project})

@login_required(login_url='/login/')
def edit_pro(request, id_project):
    """can edit a enviroment"""
    project = Project.objects.get(pk=id_project)
    if request.method == 'GET':
        # Get se usa para obtener datos y Post para enviar datos
        form = Project_Edit_Form(instance=project)
    else:
        # Aqui guardamos el cliente
        form = Project_Edit_Form(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('phase_two/project/')
    return render(request, 'edit_project.html', {'form': form})

@login_required(login_url='/login/')
def delete_pro(request, id_project):
    """delete a category"""
    project = Project.objects.get(pk=id_project)
    project.delete()
    return redirect('phase_two/project/')


@login_required(login_url='/login/')
def create_building(request):
    """delete a category"""
    if request.method == 'POST':
        form = Building_Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print("guardo")
            id_project = request.session.get('id_project')
            building = Building(
                number_builings=data['number_builings'],
                number_floors=data['number_floors'],
                id_project=id_project,
            )
            building.save()
            return redirect
        else:
            print("No valido form")
            return render(request, 'create_building.html', {'form_contact': form})
    else:
        form_contact = Building_Form()
        print("Entro a crear cont")
        return render(request, 'create_building.html', {'form_contact': form_contact})



@login_required(login_url='/login/')
def finish_pro(request):
    """delete a category"""
    id_project = request.session.get('id_project')
    project = Project.objects.get(id=id_project)
    print(project)
    contact = Contact.objects.filter(id_project=id_project)
    building = Building.objects.filter(id_project=id_project)
    return render(request, 'finish_project.html', {'project':project,
                                                   'contact':contact,
                                                   'building':building})