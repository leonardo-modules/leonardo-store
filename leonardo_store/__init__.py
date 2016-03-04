
from django.apps import AppConfig
from oscar import get_core_apps as get_eshop_apps
from django.utils.translation import ugettext_lazy as _

from .widget import *

default_app_config = 'leonardo_store.Config'


try:
    # rename original oscar search
    from oscar.apps.search import config
    config.SearchConfig.label = 'oscar_search'
except Exception:
    pass


class OscarSearchConfig(AppConfig):
    name = 'oscar.apps.search'
    verbose_name = "oscar_search"

# try change name of oscar dashboard
try:
    from oscar.apps.dashboard import config
    config.DashboardConfig.label = 'oscar_dashboard'
except:
    pass


class Default(object):

    optgroup = ('Store')

    urls_conf = 'leonardo_store.dashboard.urls'

    middlewares = [
        'oscar.apps.basket.middleware.BasketMiddleware',
    ]

    dashboard_menu = [
        'leonardo_store.dashboard.menu.store_menu',
        'leonardo_store.dashboard.menu.customers',
        'leonardo_store.dashboard.menu.analytics',
        ]

    dashboard_widgets_available = [
        'leonardo_store.dashboard.widgets.customers',
        'leonardo_store.dashboard.widgets.catalogue',
        ]

    dashboard_widgets = [
        'leonardo_store.dashboard.widgets.catalogue',
        'leonardo_store.dashboard.widgets.customers',
        ]

    def is_oscarapi_installed(self):
        try:
            import oscarapi
        except ImportError:
            pass
        else:
            return True
        return False

    @property
    def apps(self):
        oscar_apps = get_eshop_apps(['order', 'address', 'catalogue'])
        apps = []

        # if is there oscarpi include it
        if self.is_oscarapi_installed():
            apps = ['oscarapi']

        return apps + [
            'leonardo_store',
            'whoosh',
            'oscar.apps.customer',
            'leonardo_import_export',
            'django.contrib.flatpages',
            'widget_tweaks',
            'brand',
        ] + oscar_apps

    auth_backends = [
        'oscar.apps.customer.auth_backends.EmailBackend'
    ]

    context_processors = [
        'oscar.apps.promotions.context_processors.promotions',
        'oscar.apps.checkout.context_processors.checkout',
        'oscar.apps.customer.notifications.context_processors.notifications',
        'oscar.core.context_processors.metadata',
    ]

    store_profile_actions = [
        'widget/profileactions/_actions.html'
    ]

    @property
    def plugins(self):
        _plugins = []

        if self.is_oscarapi_installed():
            _plugins.append(('leonardo_store.apps.api', _('Store: API'), ),)

        return _plugins + [
            ('leonardo_store.apps.basket', _('Store: Shopping Cart'), ),
            ('leonardo_store.apps.checkout', _('Store: Checkout'), ),
            ('leonardo_store.apps.customer', _('Store: Customer Profile'), ),
            ('leonardo_store.apps.catalogue', _('Store: Product Catalog'),),
            ('leonardo_store.apps.partner', _('Store: Partners'),),
            ('leonardo_store.apps.dashboard', _('Store: Dashboard'),),
            ('leonardo_store.apps.offer', _('Store: Offers'),),
            ('leonardo_store.apps.promotions', _('Store: Promotions'),),
        ]

    widgets = [
        QuickCartWidget,
        ProductCatalogWidget,
        ProductListWidget,
        ProfileActionsWidget,
        StoreContactWidget,
        StoreActionsWidget,
        SpecialProductsWidget
    ]

    config = {
        'OSCAR_INITIAL_ORDER_STATUS': ('Pending', _('Order Initial status')),
        'OSCAR_INITIAL_LINE_STATUS': ('123456789', _('Line Initial status')),
        'OSCAR_IMAGE_FOLDER': ('eshop', _('Eshop Image Directory')),
        'OSCAR_DELETE_IMAGE_FILES': (True, _('Delete Image Files')),
        'OSCAR_PROMOTION_FOLDER': ('promotions', _('Promotions Directory')),
        'OSCAR_SHIPPING_DEFAULT_METHOD': ('first', _('Default Shipping Name')),
        'OSCAR_ALLOW_ANON_CHECKOUT': (False, _('Specifies if an anonymous user can buy products without creating an account first. If set to False users are required to authenticate before they can checkout (using Oscars default checkout views).')),
        'OSCAR_ALLOW_ANON_REVIEWS': (True, _('This setting defines whether an anonymous user can create a review for a product without registering first. If it is set to True anonymous users can create product reviews.')),
        'OSCAR_MODERATE_REVIEWS': (False, _('This defines whether reviews have to be moderated before they are publicly available. If set to False a review created by a customer is immediately visible on the product page.')),
        'OSCAR_FROM_EMAIL': ('oscar@example.com', _('The email address used as the sender for all communication events and emails handled by Oscar.')),
        'OSCAR_SEND_REGISTRATION_EMAIL': (True, _('Sending out welcome messages to a user after they have registered on the site can be enabled or disabled using this setting. Setting it to True will send out emails on registration.')),
    }

    absolute_url_overrides = {
        'catalogue.product': 'leonardo_store.overrides.oscar_product_url_app',
        'reviews.productreview': 'leonardo_store.overrides.review',
        'catalogue.category': 'leonardo_store.overrides.category',
        'wishlists.wishlist': 'leonardo_store.overrides.wishlist',
        'partner.partner': 'leonardo_store.overrides.partner',
        'offer.conditionaloffer': 'leonardo_store.overrides.offer',
    }

    navigation_extensions = [
        'leonardo_store.navigation_extensions.categories'
    ]

    css_files = [
        'oscar/css/store.css',
    ]


class Config(AppConfig, Default):
    name = 'leonardo_store'
    verbose_name = "Store"

    def ready(self):

        # monkey patch of OSCAR_HOMEPAGE
        # i don't know why is not value propagated in standard proces
        from django.conf import settings
        from .settings import OSCAR_HOMEPAGE
        settings.OSCAR_HOMEPAGE = OSCAR_HOMEPAGE

        # set model repository
        from leonardo_store.shipping.utils import set_model_repository
        set_model_repository()

        # override checkout
        from leonardo_store.payments import override_checkout
        override_checkout()

        # override catalogue
        from leonardo_store.catalogue.utils import override_catalogue
        override_catalogue()

        from leonardo_store.utils import patch_tables2
        patch_tables2()

        from leonardo_store.catalogue.dashboard import patch_product_class_attributes
        patch_product_class_attributes()

default = Default()
