
from . import methods


class Repository(object):

    '''just Payment Methods Repository'''

    @property
    def methods(self):
        '''Returns all Payment Methods which are
        subclasses from Payment Method'''

        return methods.PaymentMethod.__subclasses__()

    def get_method(self, method_code):
        '''try find method or None'''

        for method in self.methods:
            if method.code == method_code:
                return method
        return None
