from .models import ProductType, Order

def get_types_list(request):
    get_types = ProductType.objects.all()

    context = {
        'get_types': get_types
    }

    return context


def purchasing(request):
    if request.user.is_authenticated:
        order_list = Order.objects.filter(user=request.user)
        price = 0
        for i in order_list:
            price = price + i.quantity * i.product.price
    else:
        order_list = Order.objects.none()
        price = 0

    context = {
        'order_list': order_list,
        'price': price
    }
    return context