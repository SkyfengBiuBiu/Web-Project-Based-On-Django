from django.urls import path

from . import views

app_name = 'discussions'

urlpatterns = [
    path('<int:user_id>/home', views.home, name='discussion_home'),
    path('<int:discussion_id>/detail', views.datail, name='discussion_detail'),
    path('<int:user_id>/create/', views.CreateDiscussionView.as_view(), name='discussion_create'),
    path('create/done/', views.CreateDoneView.as_view(), name='create_done'),
]