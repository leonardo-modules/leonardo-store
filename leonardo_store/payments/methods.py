
from django.utils.translation import ugettext as _


class PaymentMethod(object):

    '''Base Payment Class

    All subclasses will be available on Repository.methods

    '''

    name = 'Payment Name'
    description = 'May contain HTML'
    code = 'unique'

    view = None

    def __init__(self, *args, **kwargs):

        if not self.view:
            raise Exception('Payment Method must have defined view')

        super(PaymentMethod, self).__init__(*args, **kwargs)