
from django.conf.urls import include, patterns, url
from stores.app import application

urlpatterns = patterns('',
                       url(r'^', include(application.urls)),
                       )
