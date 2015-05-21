
def oscar_product_url_app(self):
    from leonardo.module.web.widget.application.reverse import app_reverse
    return app_reverse(
        'detail',
        'leonardo_store.apps.catalog',
        kwargs={'product_slug': self.slug, 'pk': self.id})
