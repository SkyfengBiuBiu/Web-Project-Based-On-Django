from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import urlsafe_base64_decode
from django.views import generic
from django.views.decorators.cache import never_cache

from users.models import CustomUser
from .forms import CustomUserCreationForm


# Create your views here.
class SignUpView(generic.CreateView):
    template_name = 'users/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:signup_done')


class SignUpDoneView(generic.TemplateView):
    template_name = 'users/signup_done.html'


class SignUpConfirmView(generic.TemplateView):
    template_name = 'users/signup_confirm.html'
    token_generator = default_token_generator

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        self.user = self.get_user(kwargs['uidb64'])
        self.valid_link = False

        if self.user is not None:
            token = kwargs['token']
            if self.token_generator.check_token(self.user, token):
                self.user.is_active = True
                self.user.save()
                self.valid_link = True

        return super().dispatch(*args, **kwargs)

    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to byte string
            uid = urlsafe_base64_decode(uidb64).decode()
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist, ValidationError):
            user = None
        return user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['valid_link'] = self.valid_link
        context['username'] = self.user.username
        return context


def user_detail(request, user_id):
    context = {
        'content': 'User Detail Page'
    }
    return render(request, 'users/user_detail.html', context)
