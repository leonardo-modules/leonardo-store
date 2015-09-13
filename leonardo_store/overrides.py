
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


def partner(self):
    from leonardo.module.web.widget.application.reverse import app_reverse
    return app_reverse(
        'partner',
        'leonardo_store.apps.partner',
        kwargs={'code': self.code})


def offer(self):
    from leonardo.module.web.widget.application.reverse import app_reverse
    return app_reverse(
        'detail',
        'leonardo_store.apps.offer',
        kwargs={'slug': self.slug})


def review(self):
    from leonardo.module.web.widget.application.reverse import app_reverse
    kwargs = {
        'product_slug': self.product.slug,
        'product_pk': self.product.id,
        'pk': self.id
    }
    return app_reverse(
        'reviews-detail',
        'leonardo_store.apps.catalogue',
        kwargs=kwargs)


def wishlist(self):
    from leonardo.module.web.widget.application.reverse import app_reverse
    return app_reverse(
        'wishlists-detail',
        'leonardo_store.apps.customer',
        kwargs={'key': self.key})
