
from django.conf.urls import patterns

from .views import DownloadFilesView

urlpatterns = patterns('',
                       (r'^files/(?P<id>.*)/(?P<token>.*)/download/$', DownloadFilesView.as_view(),
                        {}, 'store_donwload_files'),
                       )
