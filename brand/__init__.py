
from django.apps import AppConfig


LEONARDO_APPS = ['brand']

LEONARDO_PLUGINS = [
    ('leonardo_store.apps.brand', ('Store: Brands'), ),
]


default_app_config = 'brand.Config'


class Config(AppConfig):
    name = 'brand'
    verbose_name = "Oscar Brand"
