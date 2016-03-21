
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from django.core.exceptions import PermissionDenied
from oscar.core.loading import get_model
from django.shortcuts import get_object_or_404
from .payment_handler import _extraxt_attrs

Order = get_model('order', 'order')


class DownloadFilesView(TemplateView):

    """
    Shows donwloadable items for customers which has valid transaction ID
    """

    template_name = 'customer/files.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DownloadFilesView, self).get_context_data(
            *args, **kwargs)

        files, template_name = _extraxt_attrs(self.order)

        context['files'] = files
        context['order'] = self.order
        return context

    @property
    def order(self):
        if not hasattr(self, '_order'):
            self._order = get_object_or_404(Order, number=self.kwargs['id'])
        return self._order

    def get(self, request, *args, **kwargs):

        valid = False

        # naive checking for now
        for pe in self.order.payment_events.all():
            if pe.reference == self.kwargs['token']:
                valid = True

        if not valid:
            raise PermissionDenied

        return TemplateResponse(
            request,
            self.template_name,
            context=self.get_context_data(*args, **kwargs))
