from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


# Create your views here.
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


def user_detail(request, user_id):
    context = {
        'content': 'User Detail Page'
    }
    return render(request, 'users/user_detail.html', context)
