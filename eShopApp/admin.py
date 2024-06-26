from django.contrib import admin
from .models import ProductType, Product, Order, MoreImages, Shipping

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'type', 'price']

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'is_shipped']

@admin.register(Shipping)
class AdminShipping(admin.ModelAdmin):
    list_display = ['time', 'status']

admin.site.register(ProductType)
admin.site.register(MoreImages)