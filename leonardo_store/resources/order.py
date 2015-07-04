
from import_export import resources

from oscar.core.loading import get_model

Order = get_model('order', 'Order')


class OrderResource(resources.ModelResource):

    class Meta:
        model = Order
