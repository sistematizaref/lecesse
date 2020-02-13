from django.conf.urls import url

from . import views

app_name = 'base'

urlpatterns = [
    #principal view
    url('index/', views.index, name='index'),
]