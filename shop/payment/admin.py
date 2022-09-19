from django.contrib import admin

from .models import Order, Discount



class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'buyer',
    )


admin.site.register(Discount)
admin.site.register(Order, OrderAdmin)
