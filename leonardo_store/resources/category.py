
from import_export import resources

from oscar.core.loading import get_model

Category = get_model('catalogue', 'Category')


class CategoryResource(resources.ModelResource):

    class Meta:
        model = Category
        exclude = ('image', 'numchild',)
