from django.contrib import admin
from django.urls import path

from events import views


urlpatterns = [
    path('events/<int:user_id>/home/', views.EventHomeView),
    path('events/<int:event_id>/detail/', views.EventDetailView),
    path('events/<int:user_id>/invitation/', views.EventInvitationView),
]