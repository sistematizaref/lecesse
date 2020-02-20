from django.conf.urls import url

from . import views

app_name = 'phase_one'

urlpatterns = [
    #principal view
    url('home/', views.home, name='home'),
    #view category
    url('category/', views.category, name='category'),
    url('edit-category/(?P<id_category>[0-9]+)/$', views.edit_category, name='edit_category'),
    url('delete-category/(?P<id_category>[0-9]+)/$', views.delete_category, name='delete_category'),
    url('view_category/(?P<id_category>[0-9]+)/$', views.view_category, name='view_category'),

    #view materials
    url('materials/', views.materials, name='materials'),
    url('edit-material/(?P<id_material>[0-9]+)/$', views.edit_material, name='edit_material'),
    url('delete-material/(?P<id_material>[0-9]+)/$', views.delete_material, name='delete_material'),
    url('view_material/(?P<id_material>[0-9]+)/$', views.view_material, name='view_material'),

    #view providers
    url('providers/', views.providers, name='providers'),
    url('edit-provider/(?P<id_provider>[0-9]+)/$', views.edit_provider, name='edit_provider'),
    url('delete-provider/(?P<id_provider>[0-9]+)/$', views.delete_provider, name='delete_provider'),
    url('view_provider/(?P<id_provider>[0-9]+)/$', views.view_provider, name='view_provider'),


]