from django.shortcuts import render, redirect
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from users.models import CustomUser

# Create your views here.

@login_required(login_url='/login/')
def home(request):
    """show users view"""
    users = CustomUser.objects.all()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = form.save()
            return redirect('/users/home/')
        else:
            return render(request, 'users.html', {'form': form, 'users': users})
    else:
        form = CustomUserCreationForm()
        return render(request, 'users.html', {'form': form, 'users': users})


@login_required(login_url='/login/')
def edit_user(request, id_user):
    """allow edit a user"""
    user = CustomUser.objects.get(pk=id_user)

    if request.method == 'GET':
        # Get se usa para obtener datos y Post para enviar datos
        form = CustomUserChangeForm(instance=user)
    else:
        # Aqui guardamos el cliente
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/users/home/')
    return render(request, 'edit_user.html', {'form': form})


@login_required(login_url='/login/')
def view_user(request, id_user):
    """can view data user"""
    user = CustomUser.objects.get(pk=id_user)
    return render(request, 'view_user.html', {'user': user})


@login_required(login_url='/login/')
def delete_user(request, id_user):
    """delete a user"""
    user = CustomUser.objects.get(pk=id_user)
    user.delete()
    return redirect('/users/home/')