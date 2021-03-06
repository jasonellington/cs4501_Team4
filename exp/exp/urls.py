"""exp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^exp/all/cars$', views.all_cars, name='all_cars'),
    url(r'^exp/cars/recentlyadded$', views.recently_added_cars, name='recently_added_cars'),
    url(r'^exp/cars/single_car$', views.single_car, name='single_car'),
    url(r'^exp/register$', views.register, name='register'),
    url(r'^exp/create/listing$', views.create_listing, name='create_listing'),
    url(r'^exp/login$', views.login_add_authenticator, name='login_add_authenticator'),
    url(r'^exp/get_authenticator$', views.login_get_authenticator, name='login_get_authenticator'),
    url(r'^exp/log_out$', views.log_out, name='log_out'),
    url(r'^exp/check_auth$', views.check_auth, name='check_auth'),
    url(r'^exp/search$', views.search, name='search'),
]
