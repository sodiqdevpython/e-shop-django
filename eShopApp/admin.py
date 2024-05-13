from django.contrib import admin
from .models import Profile, ProductType, Product, Comment, Order, MoreImages, Shipping

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'type', 'price']

@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ['user', 'product', 'created_at']

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['user', 'product']

@admin.register(Shipping)
class AdminShipping(admin.ModelAdmin):
    list_display = ['order', 'time', 'status']

admin.site.register(ProductType)
admin.site.register(Profile)
admin.site.register(MoreImages)