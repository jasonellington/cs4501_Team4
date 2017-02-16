from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/v1/home$', views.home_page, name='home_page'),
    url(r'^api/v1/users$', views.get_users, name='get_users'),
    url(r'^api/v1/user/([0-9]+)/$', views.get_user, name='get_user'),
    url(r'^api/v1/cars$', views.get_cars, name='get_cars'),
    url(r'^api/v1/car/([0-9]+)/$', views.get_car, name='get_car'),
    url(r'^api/v1/update/user/(?P<id>[0-9]+)/$', views.update_user, name='update_user'),
    url(r'^api/v1/create/user$', views.create_user, name='create_user'),
    url(r'^api/v1/update/car/(?P<id>[0-9]+)/$', views.update_car, name='update_car'),
    url(r'^api/v1/create/car$', views.create_car, name='create_car'),
]