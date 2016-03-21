from leonardo.utils.email import send_templated_email
from leonardo.module.web.widget.application.reverse import app_reverse


def _extraxt_attrs(order):
    '''extract file fields and template name'''

    template_name = None
    files = []

    for line in order.lines.all():
        for attr in line.product.attribute_values.all():
            if attr.attribute.is_hidden and attr.attribute.code.startswith('_file'):
                files.append(attr.value_file)
            elif attr.attribute.code == 'template_name':
                template_name = attr.value_text

        for attr in line.attributes.all():
            if attr.option.is_hidden and attr.option.code.startswith('_file'):
                files.append(attr.value)
            elif attr.option.code == 'template_name':
                template_name = attr.value

    return files, template_name


def _get_token(order):
    '''naive implementation extra db record'''
    for pe in order.payment_events.all():
        if pe.reference:
            return pe.reference


def send_files_as_mail(sender, order, user, request, response, **kwargs):
    '''Send files to customers'''

    email = order.user.email

    files, template_name = _extraxt_attrs(order)

    if not files:
        return

    context = {
        'download_url': request.site.domain + app_reverse(
            'store_donwload_files', 'leonardo_store.apps.checkout',
            args=(order.number, _get_token(order))),
        'files': [f.name for f in files]
        }

    send_templated_email(
        'Your files',
        template_name or 'customer/emails/download_files.html',
        context,
        [email],
        files=[f.path for f in files],
        fail_silently=True)

    return True
