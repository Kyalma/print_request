"""pullrequest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView


import pullapp.views.front_views as front_views
import pullapp.views.rest_views as rest_views

from pullapp.forms import SubmissionForm
from pullapp.forms import ConsumableForm

urlpatterns = [
    url(r'^$',
        login_required(
            TemplateView.as_view(template_name='pullapp/home.html')),
        name='home'),
    path('admin/', admin.site.urls),
    path('docs/',
         TemplateView.as_view(template_name='swagger-ui.html',
                              extra_context={'schema_url': 'openapi-schema'}),
         name='swagger-ui'),
    path('openapi/',
         get_schema_view(title="Your Project",
                         description="API for all things …",
                         version="1.0.0"),
         name='openapi-schema'),
    url(r'^submission/list/$', rest_views.SubmissionListGenericAPI.as_view()),
    url(r'^submission/create/$', rest_views.SubmissionCreateGenericAPI.as_view()),
    url(r'^submission/(?P<id_submission>[\w\-]+)/$', rest_views.SubmissionGenericAPI.as_view()),
    url(r'^submission/user/(?P<user_id>[\w\-]+)/list/$', rest_views.UserSubmissionListGenericAPI.as_view()),
    url(r'^consumable/list/$', rest_views.ConsumableListGenericAPI.as_view()),
    url(r'^consumable/create/$', rest_views.ConsumableCreateGenericAPI.as_view()),
    url(r'^consumable/(?P<id_material>[\w\-]+)/$', rest_views.ConsumableGenericAPI.as_view()),
    url(r'^printer/list/$', rest_views.PrinterListGenericAPI.as_view()),
    url(r'^printer/create/$', rest_views.PrinterCreateGenericAPI.as_view()),
    url(r'^printer/(?P<id_printer>[\w\-]+)/$', rest_views.PrinterGenericAPI.as_view()),
    url(r'^slice/(?P<id_submission>[\w\-]+)/$', rest_views.SlicerParamGenericAPI.as_view()),
    url(r'^signup/$', front_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(
        template_name='pullapp/login.html',
        redirect_authenticated_user=True), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^account/$',
        login_required(
            TemplateView.as_view(template_name='pullapp/account.html')),
        name='account'),
    url(r'^request/new/$',
        login_required(
            CreateView.as_view(
                template_name='pullapp/submission.html',
                form_class=SubmissionForm)),
        name='submission'),
    url(r'^material/new/$',
        login_required(
            CreateView.as_view(
                template_name='pullapp/material.html',
                form_class=ConsumableForm,
                success_url='/')),
        name='submission')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
