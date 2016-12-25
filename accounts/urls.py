from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^auth/', include('aauth.urls', namespace='auth')),
    url(r'^admin/', admin.site.urls),
]
