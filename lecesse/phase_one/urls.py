from django.conf.urls import url

from . import views

app_name = 'phase_one'

urlpatterns = [
    #principal view
    url('home/', views.home, name='home'),
    #view category
    url('category/', views.category, name='category'),
    url('edit-cate/(?P<id_category>[0-9]+)/$', views.edit_cate, name='edit_cate'),
    url('delete-cate/(?P<id_category>[0-9]+)/$', views.delete_cate, name='delete_cate'),
    url('view_cate/(?P<id_category>[0-9]+)/$', views.view_cate, name='view_cate'),

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