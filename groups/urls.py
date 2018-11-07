from django.contrib import admin
from django.urls import path

from groups import views

path('groups/<int:user_id>/home/', views.GroupHomeView),
path('groups/<int:group_id>/detail/', views.GroupDetailView),