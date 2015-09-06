
from django.conf import settings
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

    def get_default_shipping_method(self, basket, shipping_addr=None,
                                    **kwargs):
        """
        Return a 'default' shipping method to show on the basket page to give
        the customer an indication of what their order will cost.
        """

        default = getattr(settings, 'OSCAR_SHIPPING_DEFAULT_METHOD', False)

        if default and default != 'first':

            for method in self.get_available_shipping_methods(basket, shipping_addr, **kwargs):

                if method.name == default:
                    return method

        return super(ModelRepository, self).get_default_shipping_method(basket,
                                                                        shipping_addr, **kwargs)
