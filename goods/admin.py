from django.contrib import admin

from goods.models import BiddingCategories, Categories, Lots


# Register your models here.

# admin.site.register(Categories)
# admin.site.register(BiddingCateories)
# admin.site.register(Lots)

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(BiddingCategories)
class BiddingCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('format_bidding',)}


@admin.register(Lots)
class LotsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
