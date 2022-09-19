from django.contrib import admin

from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price') 
    list_filter = ('id',) 


admin.site.register(Item, ItemAdmin) 