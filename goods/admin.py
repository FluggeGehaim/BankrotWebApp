from django.contrib import admin

from goods.models import BiddingCategories, Categories, Lots



@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(BiddingCategories)
class BiddingCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('format_bidding',)}


@admin.register(Lots)
class LotsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'place', 'price', 'bidding_date', 'url_etp']
    list_editable = ['place']
    search_fields = ['name', 'place', 'bidding_date', 'category']
    list_filter = ['place', 'bidding_date', 'category', 'format_bidding']
    fields = ['name', 'category', 'description', 'place', 'price', 'bidding_date', 'format_bidding', 'url_etp', 'image', 'slug']
    