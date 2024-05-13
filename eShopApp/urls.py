from django.urls import path
from .views import home, store, filtering_products, search, detail_products

urlpatterns = [
    path('', home, name='home'),
    path('mahsulotlar/', store, name='store'),
    path('mahsulotlar/<str:name>/', filtering_products, name='filtering_products'),
    path('search/', search, name='search'),
    path('mahsulot/<int:id>/', detail_products, name='product_detail')
]