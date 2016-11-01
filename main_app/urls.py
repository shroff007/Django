from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index),
    url(r'^post_url/$',views.post_person, name = 'post_person'),
    url(r'^login/$',views.login_view, name = 'login'),
    url(r'^logout/$',views.logout_view, name = 'logout'),
]
