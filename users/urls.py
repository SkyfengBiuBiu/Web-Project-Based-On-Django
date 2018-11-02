from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    # path('', views.login, name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<int:user_id>/password_change/', views.password_change, name='password_change'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('<int:user_id>/user_detail', views.user_detail, name='user_detail')
]
