
from django.utils import six

try:
    from importlib import import_module
except ImportError:  # pragma: no cover
    from django.utils.importlib import import_module


def override_basket_tags():
    '''set ModelRepository as default Shipping Repository'''
    from oscar.templatetags import basket_tags
    from oscar.apps.basket import views
    from .forms import AddToBasketForm
    basket_tags.AddToBasketForm = AddToBasketForm
    views.AddToBasketForm = AddToBasketForm


def get_object(path, fail_silently=False):
    # Return early if path isn't a string (might already be an callable or
    # a class or whatever)
    if not isinstance(path, six.string_types):  # XXX bytes?
        return path

    try:
        return import_module(path)
    except ImportError:
        try:
            dot = path.rindex('.')
            mod, fn = path[:dot], path[dot + 1:]

            return getattr(import_module(mod), fn)
        except (AttributeError, ImportError):
            if not fail_silently:
                raise
