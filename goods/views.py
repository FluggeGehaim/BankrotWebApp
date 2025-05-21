from django.views.generic import DetailView, ListView
from django.http import Http404

from goods.models import Lots, Categories
from goods.utils import search


class CatalogView(ListView):
    model = Lots
    template_name = "goods/catalog.html"
    context_object_name = "goods"
    paginate_by = 9
    allow_empty = False

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        page = self.request.GET.get("page", 1)
        # on_sale = self.request.GET.get("on_sale")
        order_by = self.request.GET.get("order_by")
        query = self.request.GET.get("q")

        if category_slug == "all":
            lots = super().get_queryset()
        elif query:
            lots = search.q_search(query)
        else:
            lots =  super().get_queryset().filter(category__slug=category_slug)
            if not lots.exists():
                raise Http404()
        # if on_sale:
        #     lots = lots.filter(discount__gt=0)
        if order_by:
            lots = lots.order_by(order_by)

        return lots

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pagename"] = "BankrotСпец - Каталог"
        context["slug_url"] = self.kwargs.get("category_slug")
        context["categories"] = Categories.objects.all()

        return context


class LotView(DetailView):
    template_name = "goods/lot.html"
    slug_url_kwarg = "lot_slug"
    context_object_name = "lot"

    def get_object(self, queryset=None):
        lot = Lots.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return lot

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pagename"] = self.object.name
        return context
