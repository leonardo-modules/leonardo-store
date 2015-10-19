
from __future__ import absolute_import

from django.conf.urls import include, url


from oscar.apps.dashboard.app import application

urlpatterns = []

try:
    from accounts.dashboard.app import application as accounts_app

    urlpatterns += [
                    url(r'^accounts/', include(accounts_app.get_urls()))
                    ]
except Exception as e:
    pass

try:
    from brand.dashboard.app import application as brand_app

    urlpatterns += [
                    url(r'^brand/', include(brand_app.get_urls()))
                    ]
except Exception as e:
    pass


try:
    from stores.dashboard.app import application as store_app

    urlpatterns += [
                    url(r'^stores/', include(store_app.get_urls()))
                    ]
except Exception as e:
    pass

urlpatterns += [
    url(r'^', include(application.get_urls()),)
]
