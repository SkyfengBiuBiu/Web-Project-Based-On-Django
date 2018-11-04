from django.urls import path

from . import views

app_name = 'discussions'

urlpatterns = [
    path('<int:user_id>/home', views.home, name='discussion_home'),
    path('<int:discussion_id>/detail', views.datail, name='discussion_detail')
]