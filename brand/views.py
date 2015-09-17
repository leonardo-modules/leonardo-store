
from django.views import generic
from oscar.core.loading import get_model

Brand = get_model('brand', 'brand')


class ListView(generic.ListView):
    model = Brand
    template_name = 'brand/list.html'
    context_object_name = 'brand_list'


class DetailView(generic.DetailView):
    model = Brand
    template_name = 'brand/detail.html'
    context_object_name = 'brand'
