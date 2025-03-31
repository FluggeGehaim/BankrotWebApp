from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from goods.models import Lots


def catalog(request, category_slug):
    page = request.GET.get("page", 1)
    
    if category_slug == "all":
        lots = Lots.objects.all()
    else:
        lots = get_list_or_404(Lots.objects.filter(category__slug=category_slug))

    paginator = Paginator(lots,9)
    current_page = paginator.page(int(page))
    context = {
        "pagename": "BankrotСпец - Каталог",
        "goods": current_page,
    }
    return render(request, "goods/catalog.html", context)


def lot(request, lot_slug):
    lot_info = Lots.objects.get(slug=lot_slug)

    context = {
        "lot": lot_info,
    }
    return render(request, "goods/lot.html", context)

