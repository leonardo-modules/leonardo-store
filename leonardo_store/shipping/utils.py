
def set_model_repository():
    '''set ModelRepository as default Shipping Repository'''
    from leonardo_store.shipping.repository import ModelRepository
    from oscar.apps.shipping import repository
    from oscar.apps.checkout import views
    repository.Repository = ModelRepository
    views.Repository = ModelRepository
