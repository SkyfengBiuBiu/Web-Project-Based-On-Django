from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup/done/', views.SignUpDoneView.as_view(), name='signup_done'),
    path('signup/<uidb64>/<token>/', views.SignUpConfirmView.as_view(), name='signup_confirm'),

    path('<int:user_id>/profile/', views.UserProfileView.as_view(), name='profile'),
    path('<int:user_id>/settings/', views.PrivacySettingsView.as_view(), name='privacy_settings'),

    path('<int:user_id>/delete/', views.CustomUserDeleteView.as_view(), name='delete'),
    path('delete/done/', views.CustomUserDeleteDoneView.as_view(), name='delete_done'),
]
