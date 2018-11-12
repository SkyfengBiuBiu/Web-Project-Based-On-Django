from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserAdminCreationForm, CustomUserAdminChangeForm
from .models import CustomUser, CustomUserProfile


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserAdminCreationForm
    form = CustomUserAdminChangeForm
    list_display = ['email', 'username']


class CustomUserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'date_of_birth', 'photo']


# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(CustomUserProfile, CustomUserProfileAdmin)
