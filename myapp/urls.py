from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/v1/home$', views.home_page, name='api/v1/home'),
    url(r'^api/v1/users$', views.get_users, name='api/v1/users'),
    url(r'^api/v1/user/([0-9]+)/$', views.get_user, name='api/v1/user/([0-9])/$'),
]