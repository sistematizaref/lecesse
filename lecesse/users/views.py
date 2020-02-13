from django.shortcuts import render, redirect
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser

# Create your views here.


def home(request):
    """show users view"""
    users = CustomUser.objects.all()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = form.save()
            return redirect('/index/')
        else:
            return render(request, 'users.html', {'form': form, 'users': users})
    else:
        form = CustomUserCreationForm()
        return render(request, 'users.html', {'form': form, 'users': users})