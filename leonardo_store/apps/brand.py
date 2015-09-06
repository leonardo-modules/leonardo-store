
from __future__ import absolute_import

from django.conf.urls import include, patterns
from brand.app import application

urlpatterns = patterns('',
                       (r'^', include(application.get_urls()),),
                       )
