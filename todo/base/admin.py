from django.contrib import admin
from .models import Box, Item



@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'boxed',)



class ItemInline(admin.StackedInline):
    model = Item
    fields = ['name']




class BoxAdmin(admin.ModelAdmin):
    list_display = ('number', 'created', 'additional', 'get_items')
    inlines = [ItemInline]

admin.site.register(Box, BoxAdmin)