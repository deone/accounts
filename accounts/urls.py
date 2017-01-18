from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^auth/', include('aauth.urls')),
    url(r'^admin/', admin.site.urls),
]