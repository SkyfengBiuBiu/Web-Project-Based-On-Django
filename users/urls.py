from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup/done/', views.SignUpDoneView.as_view(), name='signup_done'),
    path('signup/<uidb64>/<token>/', views.SignUpConfirmView.as_view(), name='signup_confirm'),

    path('<int:user_id>/user_detail', views.user_detail, name='user_detail')
]
