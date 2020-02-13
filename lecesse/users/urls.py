from django.conf.urls import url

from . import views

app_name = 'users'

urlpatterns = [
    #principal view
    url('home/', views.home, name='home'),
]