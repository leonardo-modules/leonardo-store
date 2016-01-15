from django.utils.translation import ugettext_lazy as _
from leonardo_admin_dashboard import modules
from django.core.urlresolvers import reverse

"""
TODO: make this useful
[{'url_name': 'dashboard:index', 'icon': 'icon-th-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18bec3e50>}, {'icon': 'icon-sitemap', 'children': [{'url_name': 'dashboard:catalogue-product-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18c14aa10>}, {'url_name': 'dashboard:catalogue-class-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18c15ab90>}, {'url_name': 'dashboard:catalogue-category-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18becc850>}, {'url_name': 'dashboard:range-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18becc950>}, {'url_name': 'dashboard:stock-alert-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18beccf10>}], 'label': <django.utils.functional.__proxy__ object at 0x7fb18c14a750>}, {'icon': 'icon-shopping-cart', 'children': [{'url_name': 'dashboard:order-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18becc710>}, {'url_name': 'dashboard:order-stats', 'label': <django.utils.functional.__proxy__ object at 0x7fb18beccd90>}, {'url_name': 'dashboard:partner-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18beccd10>}], 'label': <django.utils.functional.__proxy__ object at 0x7fb18beccdd0>}, {'icon': 'icon-group', 'children': [{'url_name': 'dashboard:users-index', 'label': <django.utils.functional.__proxy__ object at 0x7fb18bed26d0>}, {'url_name': 'dashboard:user-alert-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18bed23d0>}], 'label': <django.utils.functional.__proxy__ object at 0x7fb18beccc10>}, {'icon': 'icon-bullhorn', 'children': [{'url_name': 'dashboard:offer-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18becccd0>}, {'url_name': 'dashboard:voucher-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18becce10>}], 'label': <django.utils.functional.__proxy__ object at 0x7fb18beccd50>}, {'icon': 'icon-folder-close', 'children': [{'url_name': 'dashboard:promotion-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18becc910>}, {'url_name': 'dashboard:promotion-list-by-page', 'label': <django.utils.functional.__proxy__ object at 0x7fb18becc810>}, {'url_name': 'dashboard:page-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18beccfd0>}, {'url_name': 'dashboard:comms-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18c14aa50>}, {'url_name': 'dashboard:reviews-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18bec5650>}], 'label': <django.utils.functional.__proxy__ object at 0x7fb18bed2210>}, {'url_name': 'dashboard:reports-index', 'icon': 'icon-bar-chart', 'label': <django.utils.functional.__proxy__ object at 0x7fb18becc8d0>}, {'icon': 'icon-shopping-cart', 'children': [{'url_name': 'dashboard:store-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18bed2610>}, {'url_name': 'dashboard:store-group-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18beccf50>}], 'label': <django.utils.functional.__proxy__ object at 0x7fb18bed6310>}, {'icon': 'icon-globe', 'children': [{'url_name': 'dashboard:accounts-list', 'label': 'Accounts'}, {'url_name': 'dashboard:transfers-list', 'label': 'Transfers'}, {'url_name': 'dashboard:report-deferred-income', 'label': 'Deferred income report'}, {'url_name': 'dashboard:report-profit-loss', 'label': 'Profit/loss report'}], 'label': 'Accounts'}, {'icon': 'icon-globe', 'children': [{'url_name': 'dashboard:brand-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18bede6d0>}, {'url_name': 'dashboard:brand-list', 'label': <django.utils.functional.__proxy__ object at 0x7fb18bede710>}], 'label': <django.utils.functional.__proxy__ object at 0x7fb18bede690>}]
"""

catalogue = modules.LinkList(
    _('Catalogue'),
    children=[
        [_('Products'), reverse('dashboard:catalogue-category-list')],
        [_('Product Types'), reverse('dashboard:catalogue-class-list'), 'icon-data'],
        [_('Categories'), reverse('dashboard:catalogue-category-list'), 'icon-book'],
    ],
    column=2,
    order=1
)
orders = modules.LinkList(
    _('Orders'),
    children=[
        [_('Orders'), reverse('dashboard:order-list'), 'icon-book'],
        [_('Orders Stats'), reverse('dashboard:order-stats'), 'icon-book'],
    ],
    column=2,
    order=1
)

reports = modules.LinkList(
    _('Reports'),
    children=[
        [_('Reports'), reverse('dashboard:reports-index'), 'icon-book'],
    ],
    column=2,
    order=1
)

marketing = modules.LinkList(
    _('Marketing'),
    children=[
        [_('Promotions'), reverse('dashboard:promotion-list'), 'icon-book'],
    ],
    column=2,
    order=1
)

stocks = modules.LinkList(
    _('Stocks'),
    children=[
        [_('Stock Alerts'), reverse('dashboard:stock-alert-list')],
    ]
    )

customers = modules.ModelList(
    _('Store'),
    models=('auth.user', 'customer.*', 'address.*', 'whishlists.*'),
    column=2,
    order=5
)
