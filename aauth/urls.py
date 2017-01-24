from django.conf.urls import url

from .views import login

urlpatterns = [
    url(r'^login/$', login, name='aauth_login'),
]