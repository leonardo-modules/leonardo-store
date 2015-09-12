
from django.db.transaction import atomic, savepoint, savepoint_rollback
from import_export import fields, resources, widgets
from import_export.resources import *
from oscar.core.loading import get_model

from ._utils import import_data
from .fields import CategoryField, StockRecordsField, AttributeField

Product = get_model('catalogue', 'Product')
ProductImage = get_model('catalogue', 'ProductImage')
ProductClass = get_model('catalogue', 'ProductClass')
Partner = get_model('partner', 'Partner')

PRODUCT_FIELDS = (
    'id', 'upc', 'parent', 'title', 'slug',
    'description',
    'product_class', 'partner', 'categories',
    'rating', 'is_discountable',)


class ProductResource(resources.ModelResource):

    categories = CategoryField('productcategory_set', column_name='categories')

    parent = fields.Field('parent',
                          column_name='parent',
                          widget=widgets.ForeignKeyWidget(
                              Product, field='slug'))

    partner = StockRecordsField('partner', column_name='partner')
    partner_sku = StockRecordsField('partner_sku', column_name='partner_sku')

    cost_price = StockRecordsField(
        'cost_price',
        column_name='cost_price',
        widget=widgets.DecimalWidget())

    price_retail = StockRecordsField(
        'price_retail',
        column_name='price_retail',
        widget=widgets.DecimalWidget())

    price_excl_tax = StockRecordsField(
        'price_excl_tax',
        column_name='price_excl_tax',
        widget=widgets.DecimalWidget())

    price_currency = StockRecordsField(
        'price_currency',
        column_name='price_currency')

    num_in_stock = StockRecordsField(
        'num_in_stock',
        column_name='num_in_stock',
        widget=widgets.IntegerWidget())

    low_stock_threshold = StockRecordsField(
        'low_stock_threshold',
        column_name='low_stock_threshold',
        widget=widgets.IntegerWidget())

    num_allocated = StockRecordsField(
        'num_allocated',
        column_name='num_allocated',
        widget=widgets.IntegerWidget())

    price_tax = AttributeField(
        'price_tax',
        column_name='price_tax',
        widget=widgets.DecimalWidget())

    product_class = fields.Field('product_class',
                                 column_name='product_class',
                                 widget=widgets.ForeignKeyWidget(
                                     ProductClass, field='slug'))

    rating = fields.Field('rating',
                          column_name='rating',
                          widget=widgets.DecimalWidget())

    import_data = import_data

    class Meta:
        model = Product
        fields = PRODUCT_FIELDS
        export_order = PRODUCT_FIELDS
        import_id_fields = ('upc', 'id')


class ProductImageResource(resources.ModelResource):

    class Meta:
        model = ProductImage
        fields = (
            'product', 'product__upc', 'product__title', 'original', 'caption',
            'display_order', )
        import_id_fields = ('product',)
