
from import_export import resources

from oscar.core.loading import get_model

Category = get_model('catalogue', 'Category')
ProductCategory = get_model('catalogue', 'ProductCategory')


class CategoryResource(resources.ModelResource):

    class Meta:
        model = Category
        exclude = ('image', 'numchild',)


PRODUCT_CATEGORY_FIELDS = ('id', 'product', 'product__title',
                           'category', 'category__name')


class ProductCategoryResource(resources.ModelResource):

    class Meta:
        model = ProductCategory
        fields = PRODUCT_CATEGORY_FIELDS
        export_order = PRODUCT_CATEGORY_FIELDS
