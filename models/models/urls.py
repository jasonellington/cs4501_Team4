from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/home$', views.home_page, name='home_page'),
    url(r'^api/v1/details$', views.details, name='details'),
    url(r'^api/v1/users$', views.get_users, name='get_users'),
    url(r'^api/v1/user/(?P<user_id>[0-9]+)/$', views.get_user, name='get_user'),
    url(r'^api/v1/userid/(?P<user_id>[a-zA-Z0-9]+)/$', views.get_user_id, name='get_user_id'),
    url(r'^api/v1/password/(?P<user_id>[a-zA-Z0-9]+)/$', views.get_password, name='get_password'),
    url(r'^api/v1/delete/user/([0-9]+)/$', views.delete_user, name='delete_user'),
    url(r'^api/v1/cars$', views.get_cars, name='get_cars'),
    url(r'^api/v1/cars/recentlyadded$', views.get_recently_added_cars, name='get_recently_added_cars'),
    url(r'^api/v1/car/(?P<car_id>[0-9]+)/$', views.get_car, name='get_car'),
    url(r'^api/v1/delete/car/([0-9]+)/$', views.delete_car, name='delete_car'),
    url(r'^api/v1/update/user/(?P<id>[a-zA-Z0-9]+)/$', views.update_user, name='update_user'),
    url(r'^api/v1/create/user$', views.create_user, name='create_user'),
    url(r'^api/v1/update/car/(?P<id>[0-9]+)/$', views.update_car, name='update_car'),
    url(r'^api/v1/create/car$', views.create_car, name='create_car'),
    url(r'^api/v1/add_auth$', views.add_auth, name='add_auth'),
    url(r'^api/v1/delete_auth$', views.delete_auth, name='delete_auth'),
    url(r'^api/v1/auths$', views.get_auths, name='get_auths'),
    url(r'^api/v1/check_auth/(?P<authenticator>[a-zA-Z0-9]+)/$', views.check_auth, name='check_auth'),
]