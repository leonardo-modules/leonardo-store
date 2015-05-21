from django.conf.urls.defaults import patterns

urlpatterns = patterns('webcms.module.store.ext.branch.views',
    (r'^$', 'branch_list', {'region': None}, "webcms_store_branch_list"),
    (r'^(?P<region>[\w\-]+)/$', 'branch_list', {}, "webcms_store_branch_region_list"),
    (r'^(?P<region>[\w\-]+)/(?P<slug>[\w\-]+)/$', 'branch_detail', {}, "webcms_store_branch_detail"),
)
