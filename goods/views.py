from django.shortcuts import render
from goods.models import Lots


def catalog(request):
    lots = Lots.objects.all()
    context = {
        "pagename": "BankrotСпец - Каталог",
        "goods": lots,
    }
    return render(request, "goods/catalog.html", context)


def lot(request):
    return render(request, "goods/lot.html")
