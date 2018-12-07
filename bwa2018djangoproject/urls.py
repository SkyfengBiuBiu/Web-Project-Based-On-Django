"""bwa2018djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import re

from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from profiles.views import MyHomeView

urlpatterns = [
    path('', MyHomeView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('profiles/', include('profiles.urls')),
    path('discussions/', include('discussions.urls')),
    path('friendships/', include('friendships.urls')),
]


def customized_static(prefix, view=serve, **kwargs):
    return [
        re_path(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')), view, kwargs=kwargs),
    ]


urlpatterns += customized_static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
