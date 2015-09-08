
def override_catalogue():
    '''set ModelRepository as default Shipping Repository'''
    from oscar.apps.catalogue import views
    from .views import CatalogueView
    views.CatalogueView = CatalogueView
