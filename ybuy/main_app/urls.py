
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^', views.Home),
    url(r'^rentee/$', views.Rentee),
    url(r'^renter/$', views.Renter),
]
