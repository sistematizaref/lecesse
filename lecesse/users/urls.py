from django.conf.urls import url

from . import views

app_name = 'users'

urlpatterns = [
    #principal view
    url('home/', views.home, name='home'),
    #edit user view
    url('edit-user/(?P<id_user>[0-9]+)/$', views.edit_user, name='edit_user'),
    #edit user view
    url('delete-user/(?P<id_user>[0-9]+)/$', views.delete_user, name='delete_user'),
    #user view
    url('view-user/(?P<id_user>[0-9]+)/$', views.view_user, name='view_user'),
]