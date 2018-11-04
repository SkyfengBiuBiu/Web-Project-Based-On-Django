from django.urls import path

from . import views

app_name = 'friendships'

urlpatterns = [
    path('<int:user_id>/home', views.home, name='friendship_home'),
    path('<int:user_id>/request', views.request, name='friendship_request')
]