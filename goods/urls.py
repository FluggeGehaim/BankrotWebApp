from django.urls import path
from . import views

app_name = "goods"

urlpatterns = [
    path("search/", views.catalog, name="search"),
    path("<slug:category_slug>/", views.catalog, name="index"),
    path("lot/<slug:lot_slug>/", views.lot, name="lot"),
]
