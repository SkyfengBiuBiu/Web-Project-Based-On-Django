from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    # path('', views.login, name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<int:user_id>/user_detail', views.user_detail, name='user_detail')
]
