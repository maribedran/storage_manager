from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^storage/', include('src.storage.urls', namespace='storage')),
    url(r'^suply/', include('src.suply.urls', namespace='suply')),
]
