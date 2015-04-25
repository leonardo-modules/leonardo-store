from django.conf.urls.defaults import patterns

urlpatterns = patterns('webcms.module.store.ext.feed.views',
    (r'^$', 'feed_list', {}, "webcms_store_feed_list"),
    (r'^(?P<service>[\-\w\.]+)/$', 'feed_detail', {}, "webcms_store_feed_detail"),
)
