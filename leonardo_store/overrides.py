
def oscar_product_url_app(self):
    from leonardo.module.web.widget.application.reverse import app_reverse
    return app_reverse(
        'detail',
        'leonardo_store.apps.catalogue',
        kwargs={'product_slug': self.slug, 'pk': self.id})


def category(self):
    from leonardo.module.web.widget.application.reverse import app_reverse
    return app_reverse(
        'category',
        'leonardo_store.apps.catalogue',
        kwargs={'category_slug': self.slug, 'pk': self.pk})
