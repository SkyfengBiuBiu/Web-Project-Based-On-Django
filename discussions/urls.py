from django.urls import path

from . import views

app_name = 'discussions'

urlpatterns = [
    path('<int:user_id>/home', views.home, name='discussion_home'),
    path('<int:discussion_id>/detail', views.datail, name='discussion_detail'),
    path('create/', views.CreateDiscussionView.as_view(), name='discussion_create'),
    path('<int:discussion_id>/<int:user_id>/leave', views.leave, name='discussion_confirm_leave'),
]