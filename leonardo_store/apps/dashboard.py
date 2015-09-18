
from django.conf.urls import include, patterns, url


from oscar.apps.dashboard.app import application

urlpatterns = []

try:
    from accounts.dashboard.app import application as accounts_app

    urlpatterns += patterns('',
                            (r'^accounts/', include(accounts_app.urls)),
                            )
except ImportError:
    pass

urlpatterns += patterns('',
                        (r'^', include(application.get_urls()),),
                        )
