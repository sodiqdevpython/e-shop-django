from .models import ProductType

def get_types_list(request):
    get_types = ProductType.objects.all()

    context = {
        'get_types': get_types
    }

    return context