
from oscar.apps.catalogue.abstract_models import *  # noqa

from .abstract_models import AbstractOption, AbstractProductAttribute

__all__ = []


class Option(AbstractOption):

    pass

__all__.append('Option')


class ProductAttribute(AbstractProductAttribute):

    pass

__all__.append('ProductAttribute')

from oscar.apps.catalogue.models import *
