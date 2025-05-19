from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from goods.models import Lots
from goods.utils import search


def catalog(request, category_slug=None):
    page = request.GET.get("page", 1)
    # on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)
    
    if category_slug == "all":
        lots = Lots.objects.all()
    elif query:
        lots = search.q_search(query)
    else:
        lots = Lots.objects.filter(category__slug=category_slug)
        if not lots.exists():
            raise Http404()
        
    # if on_sale:
    #     lots = lots.filter(discount__gt=0)
    if order_by:
        lots = lots.order_by(order_by)
        

    paginator = Paginator(lots,9)
    current_page = paginator.page(int(page))
    context = {
        "pagename": "BankrotСпец - Каталог",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def lot(request, lot_slug):
    lot_info = Lots.objects.get(slug=lot_slug)

    context = {
        "lot": lot_info,
    }
    return render(request, "goods/lot.html", context)

