# coding: utf-8
from __future__ import absolute_import, unicode_literals
from django.core.urlresolvers import reverse
from django.utils.html import escape
from django.utils.safestring import mark_safe
import warnings
from django_tables2.utils import A


def render(self, value, record, bound_column):  # pylint: disable=W0221
    viewname = (self.viewname.resolve(record)
                if isinstance(self.viewname, A)
                else self.viewname)

    # The following params + if statements create optional arguments to
    # pass to Django's reverse() function.
    params = {}
    if self.urlconf:
        params['urlconf'] = (self.urlconf.resolve(record)
                             if isinstance(self.urlconf, A)
                             else self.urlconf)
    if self.args:
        params['args'] = [a.resolve(record) if isinstance(a, A) else a
                          for a in self.args]
    if self.kwargs:
        params['kwargs'] = {}
        for key, val in self.kwargs.items():
            # If we're dealing with an Accessor (A), resolve it, otherwise
            # use the value verbatim.
            params['kwargs'][str(key)] = (val.resolve(record)
                                          if isinstance(val, A) else val)
    if self.current_app:
        params['current_app'] = (self.current_app.resolve(record)
                                 if isinstance(self.current_app, A)
                                 else self.current_app)
    return self.render_link(reverse(viewname, **params), text=value)
