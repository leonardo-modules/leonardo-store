import warnings
from django.contrib import messages
from django.core.paginator import InvalidPage
from django.utils.http import urlquote
from django.http import HttpResponsePermanentRedirect, Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, TemplateView
from django.utils.translation import ugettext_lazy as _

from oscar.core.loading import get_class, get_model
from oscar.apps.catalogue.signals import product_viewed
from .forms import OrderByForm

Product = get_model('catalogue', 'product')
ProductReview = get_model('reviews', 'ProductReview')
Category = get_model('catalogue', 'category')
ProductAlert = get_model('customer', 'ProductAlert')
ProductAlertForm = get_class('customer.forms', 'ProductAlertForm')
get_product_search_handler_class = get_class(
    'catalogue.search_handlers', 'get_product_search_handler_class')

from oscar.apps.partner.strategy import Selector


def get_strategy(request):

    user = getattr(request, 'user', None)

    return Selector().strategy(request, user=user)


class CatalogueView(TemplateView):

    """
    Browse all products in the catalogue
    """
    context_object_name = "products"
    template_name = 'catalogue/browse.html'

    def get(self, request, *args, **kwargs):
        try:
            self.search_handler = self.get_search_handler(
                self.request.GET, request.get_full_path(), [])
        except InvalidPage:
            # Redirect to page one.
            messages.error(request, _('The given page number was invalid.'))
            return redirect('catalogue:index')
        return super(CatalogueView, self).get(request, *args, **kwargs)

    def get_search_handler(self, *args, **kwargs):
        return get_product_search_handler_class()(*args, **kwargs)

    def get_data(self):
        return self.search_handler.get_queryset()

    def get_filtered_data(self):

        data = self.get_data()

    def get_context_data(self, **kwargs):
        ctx = {}
        ctx['summary'] = _("All products")

        strategy = get_strategy(self.request)
        ctx[self.context_object_name] = data = self.get_data()

        '''
        - ``price``: a pricing policy object.
        - ``availability``: an availability policy object.
        - ``stockrecord`
        '''
        form = OrderByForm(self.request.GET)
        ctx['form'] = form

        if form.is_valid():
            order_by = form.cleaned_data.get('order_by', None)
            if order_by:
                reverse = False
                parsed = order_by.split('-')
                if len(parsed) > 1:
                    reverse = True
                    by = parsed[1]
                else:
                    by = parsed[0]

                products = sorted(data, key=lambda p:
                                  getattr(strategy.fetch_for_product(p), by, None),
                                  reverse=reverse)

                ctx[self.context_object_name] = products

        return ctx
