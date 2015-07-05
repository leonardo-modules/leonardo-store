
from import_export import resources

from oscar.core.loading import get_model

from ._utils import import_data

Product = get_model('catalogue', 'Product')


class ProductResource(resources.ModelResource):

    # patch import data
    import_data = import_data

    class Meta:
        model = Product
        fields = (
            'id', 'upc', 'parent', 'title', 'slug',
            'description', 'rating', 'is_discountable')
        import_id_fields = ('upc', 'id')
