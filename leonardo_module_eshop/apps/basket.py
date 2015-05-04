
from django.conf.urls import include, patterns, url
from oscar.apps.basket.app import application

from feincms.views.decorators import standalone

urlpatterns = patterns('',
    (r'^', include(application.get_urls()),),
)
