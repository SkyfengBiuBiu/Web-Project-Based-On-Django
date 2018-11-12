from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import urlsafe_base64_decode
from django.views import generic
from django.views.decorators.cache import never_cache

from users.models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserProfileFormSet

decorators = [never_cache, login_required]


# Create your views here.
class SignUpView(generic.CreateView):
    template_name = 'users/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:signup_done')

    def form_valid(self, form):
        form.request = self.request
        return super().form_valid(form)


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


@method_decorator(login_required, name='dispatch')
class UserProfileView(generic.UpdateView):
    template_name = 'users/user_profile.html'
    pk_url_kwarg = 'user_id'
    form_class = CustomUserChangeForm

    def form_valid(self, form):
        context = self.get_context_data()
        profile = context['profile']
        with transaction.atomic():
            self.object = form.save()

            if profile.is_valid():
                profile.instance = self.object
                profile.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['profile'] = CustomUserProfileFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['profile'] = CustomUserProfileFormSet(instance=self.object)
        return context

    def get_object(self, queryset=None):
        return CustomUser.objects.get(pk=self.kwargs[UserProfileView.pk_url_kwarg])

    def get_success_url(self):
        messages.success(self.request, 'Your information saved.')
        return reverse_lazy('users:profile', kwargs=self.kwargs)


@method_decorator(login_required, name='dispatch')
class CustomUserDeleteView(generic.DeleteView):
    template_name = 'users/user_confirm_delete.html'
    pk_url_kwarg = 'user_id'
    model = CustomUser
    success_url = reverse_lazy('users:delete_done')


class CustomUserDeleteDoneView(generic.TemplateView):
    template_name = 'users/user_delete_done.html'
