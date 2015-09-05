

from oscar.apps.shipping import repository


class ModelRepository(repository.Repository):

    '''Uses WeightBased shipping methods
    '''

    def get_available_shipping_methods(
            self, basket, shipping_addr=None, **kwargs):
        """
        Return a list of all applicable shipping method instances for a given
        basket, address etc. This method is intended to be overridden.
        """
        from oscar.apps.shipping.models import WeightBased
        return WeightBased.objects.all()
