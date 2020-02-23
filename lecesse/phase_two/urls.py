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
    url('create_apartment_tree/', views.create_apartment_tree, name='create_apartment_tree'),
    url('create_apartment_finish/', views.create_apartment_finish, name='create_apartment_finish'),
    url('edit-apartment/(?P<id_apartment>[0-9]+)/$', views.edit_apartment, name='edit_apartment'),
    url('delete-apartment/(?P<id_apartment>[0-9]+)/$', views.delete_apartment, name='delete_apartment'),
    url('view_apartment/(?P<id_apartment>[0-9]+)/$', views.view_apartment, name='view_apartment'),


    #view providers
    url('project/', views.project, name='project'),
    url('create_pro/', views.create_pro, name='create_pro'),
    url('edit-pro/(?P<id_project>[0-9]+)/$', views.edit_pro, name='edit_pro'),
    url('delete-pro/(?P<id_project>[0-9]+)/$', views.delete_pro, name='delete_pro'),
    url('view_pro/(?P<id_project>[0-9]+)/$', views.view_pro, name='view_pro'),

    #contact
    url('create_cont/', views.create_cont, name='create_cont'),



    url('create_building/', views.create_building, name='create_building'),

    url('finish_pro/', views.finish_pro, name='finish_pro'),

]

