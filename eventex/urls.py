from django.conf.urls import url
from django.contrib import admin

from eventex.core.views import home

urlpatterns = [
    url(r'^$', home),
 #   url(r'^incricao/$', subscribe),
    url(r'^admin/', admin.site.urls),
]
