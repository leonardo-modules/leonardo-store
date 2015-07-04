
from import_export import resources

from oscar.core.loading import get_model

Partner = get_model('partner', 'Partner')
StockRecord = get_model('partner', 'StockRecord')


class PartnerResource(resources.ModelResource):

    class Meta:
        model = Partner


STOCK_RECORD_FIELDS = ('id', 'product', 'product__title', 'partner',
                       'partner__name', 'product__categories',
                       'partner_sku', 'price_currency', 'price_excl_tax',
                       'price_retail',  'cost_price', 'num_in_stock',
                       'num_allocated', 'low_stock_threshold')


class StockRecordResource(resources.ModelResource):

    class Meta:
        model = StockRecord
        fields = STOCK_RECORD_FIELDS
        export_order = STOCK_RECORD_FIELDS
