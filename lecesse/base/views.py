from django.shortcuts import render

# Create your views here.

def index(request):
    """show index view"""
    return render(request, 'index.html')