from django.contrib import admin

from .models import Discount, ItemInCart, Order


class ItemInCartAdmin(admin.StackedInline):
    model = ItemInCart
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemInCartAdmin]
    list_display = ("buyer",)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ("name", "percent_off", "amount_off", "expires_at")


admin.site.register(Discount, DiscountAdmin)
admin.site.register(Order, OrderAdmin)
