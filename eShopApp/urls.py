from django.urls import path
from .views import home, store, filtering_products, search, detail_products, checkout, delete_order, login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('mahsulotlar/', store, name='store'),
    path('mahsulotlar/<str:name>/', filtering_products, name='filtering_products'),
    path('search/', search, name='search'),
    path('mahsulot/<int:id>/', detail_products, name='product_detail'),
    path('checkout/', checkout, name='checkout'),
    path('delete_order/<int:id>/', delete_order, name='delete_order'),
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]