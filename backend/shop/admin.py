from django.contrib import admin
from .models import Shop, Address, Photo


# Register your models here.

class ShopModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'shop_owner', 'slug']


admin.site.register(Shop, ShopModelAdmin)
