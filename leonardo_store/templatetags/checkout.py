
from django import template as django_template

register = django_template.Library()


@register.simple_tag
def checkout_nav(request):
    """
    {% checkout_nav request %}
    """
    try:
        fragments = request._feincms_fragments
    except:
        fragments = {}

    return fragments.get("_current_brand", '')
