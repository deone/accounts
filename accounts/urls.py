from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^auth/', include('aauth.urls')),
    url(r'^accounts/', include('core.urls')),
    url(r'^admin/', admin.site.urls),
]