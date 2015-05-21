
from __future__ import absolute_import

from django.conf.urls import include, patterns

from paypal.express import urls as paypal_urls

urlpatterns = patterns('',
                       (r'^', include(paypal_urls)),
                       )
