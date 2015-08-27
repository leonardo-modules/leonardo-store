
from django.conf.urls import include, patterns, url

urlpatterns = patterns('leonardo_store.ext.partner.views',
                       (r'^$', 'partner_list', {}, 'store_partner_list'),
                       (r'^(?P<name>.*)/$', 'partner_detail',
                        {}, 'store_partner_detail'),
                       )
