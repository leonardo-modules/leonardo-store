
from django.conf.urls import include, patterns, url


from oscar.apps.catalogue.app import application
from feincms.views.decorators import standalone

from oscar.apps.catalogue import views

# mark to standalone
views.ProductDetailView.get = standalone(views.ProductDetailView.get)


urlpatterns = patterns('',
    (r'^', include(application.get_urls()),),
)
