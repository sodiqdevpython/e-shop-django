from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Product, MoreImages, Order
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import CreateOrderForm, ShippingForm
from django.contrib import messages


def home(request):
    get_data_header = Product.objects.all().order_by('-id')[:3]
    last_products = Product.objects.all().order_by('-id')[:4][::-1]
    cheaper_products1 = Product.objects.all().order_by('price')[0:3]
    most_purchased1 = Product.objects.all().order_by('?')[:3]
    most_purchased2 = Product.objects.all().order_by('?')[4:6]

    context = {
        'get_data_header': get_data_header,
        'last_products': last_products,
        'cheaper_products1': cheaper_products1,
        'most_purchased1': most_purchased1,
        'most_purchased2': most_purchased2
    }

    return render(request, 'index.html', context)


def store(request):
    data = Product.objects.all()
    paginate = Paginator(data, 9)
    page = request.GET.get('page')
    page_obj = paginate.get_page(page)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'store.html', context)


def filtering_products(request, name):
    data = Product.objects.filter(type__name=name)
    paginate = Paginator(data, 10)
    page = request.GET.get('page')
    page_obj = paginate.get_page(page)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'store.html', context)


def search(request):
    searched_for = request.GET.get('q')
    page_obj = Product.objects.filter(
        Q(name__icontains=searched_for) | Q(info__icontains=searched_for)
    )

    context = {
        'page_obj': page_obj
    }

    return render(request, 'store.html', context)


def detail_products(request, id):
    data = get_object_or_404(Product, id=id)
    related_products = Product.objects.filter(type__name=data.type.name)
    more_images = MoreImages.objects.filter(product=data)

    if request.method == "POST" and request.user.is_authenticated:
        form = CreateOrderForm(request.POST or None)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.user = request.user
            new_order.product = data
            new_order.save()
            messages.success(request, "Sizda ushbu mahsulotdan bor")
            return redirect('product_detail', id)
    else:
        form = CreateOrderForm()

    context = {
        'data': data,
        'related_products': related_products,
        'more_images': more_images,
        'form': form
    }

    return render(request, 'product.html', context)


def login(request):
    return render(request, 'auth/login.html')

@login_required
def checkout(request):
    user_orders = Order.objects.filter(user=request.user, is_shipped=False)
    if request.method == 'POST':
        form = ShippingForm(request.POST or None)
        if form.is_valid():
            form.save()
            Order.objects.filter(user=request.user, is_shipped=False).update(is_shipped=True)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = ShippingForm()

    context = {
        'form': form,
        'user_orders': user_orders
    }

    return render(request, 'checkout.html', context)


@login_required
def delete_order(request, id):
    if request.method == 'POST':
        data = get_object_or_404(Order, id=id)
        data.delete()
        return redirect('checkout')