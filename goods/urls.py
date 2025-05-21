from django.urls import path
from . import views

app_name = "goods"

urlpatterns = [
    path("search/", views.CatalogView.as_view(), name="search"),
    path("<slug:category_slug>/", views.CatalogView.as_view(), name="index"),
    path("lot/<slug:lot_slug>/", views.LotView.as_view(), name="lot"),
]
