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
from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from rest_framework_swagger.views import get_swagger_view

from pullapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^docs/$', get_swagger_view(title='Print Request API')),
    url(r'^submission/list/$', views.SubmissionListGenericAPI.as_view()),
    url(r'^submission/create/$', views.SubmissionCreateGenericAPI.as_view()),
    url(r'^submission/(?P<id_submission>\d+)/$',
        views.SubmissionGenericAPI.as_view()),
    url(r'^submission/user/(?P<user_id>\d+)/list/$',
        views.UserSubmissionListGenericAPI.as_view()),
    url(r'^consumable/list/$', views.ConsumableListGenericAPI.as_view()),
    url(r'^consumable/create/$', views.ConsumableCreateGenericAPI.as_view()),
    url(r'^consumable/(?P<id_consumable>\d+)/$',
        views.ConsumableGenericAPI.as_view()),
    url(r'^printer/list/$', views.PrinterListGenericAPI.as_view()),
    url(r'^printer/create/$', views.PrinterCreateGenericAPI.as_view()),
    url(r'^printer/(?P<id_printer>\d+)/$', views.PrinterGenericAPI.as_view()),
    url(r'^slice/(?P<id_submission>\d+)/$',
        views.SlicerParamGenericAPI.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
