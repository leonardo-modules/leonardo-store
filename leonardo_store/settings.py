
from oscar.defaults import *
import os

OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
}

OSCAR_IMAGE_FOLDER = 'eshop'
OSCAR_PROMOTION_FOLDER = 'promotions'
OSCAR_DELETE_IMAGE_FILES = True

# search
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

OSCAR_HOMEPAGE = "/"

# insecure
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'