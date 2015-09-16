from __future__ import unicode_literals

import StringIO

from cgi import escape
from django.conf import settings
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from oscar.core.loading import get_model
from xhtml2pdf import pisa
from xhtml2pdf.pdf import pisaPDF
from django.utils.encoding import smart_str, smart_unicode


class PDFTemplateResponse(TemplateResponse):

    def generate_pdf(self, retval):

        html = smart_unicode(self.content)

        result = StringIO.StringIO()

        # convert HTML to PDF
        pisaStatus = pisa.CreatePDF(
            html,                # the HTML to convert
            dest=result,
            encoding='UTF-8')           # file handle to recieve result

        if pisaStatus.err:
            return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
        else:
            self.content = result.getvalue()

    def __init__(self, *args, **kwargs):
        kwargs['content_type'] = 'application/pdf'
        super(PDFTemplateResponse, self).__init__(
            *args, **kwargs)
        self.add_post_render_callback(self.generate_pdf)


class PDFTemplateView(TemplateView):
    response_class = PDFTemplateResponse

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        response = self.render_to_response(context)
        #response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
        return response

Order = get_model("order", "Order")


class OrderPdfView(PDFTemplateView):
    template_name = 'dashboard/orders/pdf/order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderPdfView, self).get_context_data(**kwargs)

        order = Order.objects.get(id=self.kwargs.get('id'))

        voucher_codes = []
        for discount in order.discounts.all():
            if discount.voucher_code:
                voucher_codes.append(discount.voucher_code)

        context.update({
            'order': order,
            'STATIC_ROOT': settings.STATIC_ROOT,
            'voucher_codes': voucher_codes,
        })

        return context
