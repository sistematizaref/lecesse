from django.conf.urls import url

from . import views

app_name = 'phase_two'

urlpatterns = [
    #principal view
    url('home/', views.home, name='home'),
    #view category
    url('environments/', views.environment, name='environments'),
    url('edit-enviroment/(?P<id_enviroment>[0-9]+)/$', views.edit_enviroment, name='edit_enviroment'),
    url('delete-enviroment/(?P<id_enviroment>[0-9]+)/$', views.delete_enviroment, name='delete_enviroment'),
    url('view-enviroment/(?P<id_enviroment>[0-9]+)/$', views.view_enviroment, name='view_enviroment'),

    #view materials
    url('model_apartment/', views.model_apartment, name='model_apartment'),

    url('create_apartment/', views.create_apartment, name='create_apartment'),


    #view providers
    url('project/', views.project, name='project'),



]