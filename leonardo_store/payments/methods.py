
from django.utils.translation import ugettext as _


class PaymentMethod(object):

    '''Base Payment Class

    All subclasses will be available on Repository.methods

    '''

    name = 'Payment Name'
    description = 'May contain HTML'
    code = 'unique'

    view = None

    # custom template which will be rendered
    template_name = None
