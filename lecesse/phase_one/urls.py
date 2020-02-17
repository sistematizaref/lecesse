from django.conf.urls import url

from . import views

app_name = 'phase_one'

urlpatterns = [
    #principal view
    url('home/', views.home, name='home'),
    #view category
    url('category/', views.category, name='category'),
    #view materials
    url('materials/', views.materials, name='materials'),
    #view providers
    url('providers/', views.providers, name='providers'),
    # view subcategory
    url('subcategory/', views.subcategory, name='subcategory'),
]