from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories
# Create your views here.


def index(request):

    categories = Categories.objects.all()

    context = {"pagename": "BankrotСпец - Главная", 
               "content": "Имущество с Торгов",
               'categories': categories}

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "pagename": "BankrotСпец - О нас",
        "content": "О нас", 
        "text_about_us": "Тестовый текст , информация о ресурсе"
        }
    return render(request, "main/about.html", context)
