from django.contrib import admin

from .models import Cart


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = ['lot', 'created_at']
    search_fields = ['lot', 'created_at']
    readonly_fields = ['created_at']
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'lot_display', 'created_at']
    search_fields = ['user', 'lot', 'created_at']
    list_filter = ['created_at']
    
    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return 'Аноним'
    
    def lot_display(self, obj):
        return str(obj.lot.name)
