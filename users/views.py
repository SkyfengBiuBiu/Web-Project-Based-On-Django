from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


# Create your views here.
def login(request):
    context = {
        'content': 'Login Page'
    }
    return render(request, 'users/templates/registration/login.html', context)


def password_change(request, user_id):
    context = {
        'content': 'Password Change Page'
    }
    return render(request, 'users/password_change.html', context)


def password_reset(request):
    context = {
        'content': 'Password Reset Page'
    }
    return render(request, 'users/password_reset.html', context)


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


def user_detail(request, user_id):
    context = {
        'content': 'User Detail Page'
    }
    return render(request, 'users/user_detail.html', context)
