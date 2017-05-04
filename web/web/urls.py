"""web URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', views.home_page, name='home_page'),
    url(r'^details$', views.details, name='details'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^create_listing$', views.create_listing, name='create_listing'),
    url(r'^logged_in$', views.logged_in, name='logged_in'),
    url(r'^cookie$', views.cookie, name='cookie'),
    url(r'^log_out$', views.log_out, name='log_out'),
    url(r'^search_results$', views.search_results, name='search_results'),
    url(r'^search$', views.search, name='search'),
    url(r'^single_listing_result$', views.single_listing_result, name='single_listing_result'),
    url(r'^single_listing/(?P<id>[0-9]+)$', views.single_listing, name='single_listing')
]
