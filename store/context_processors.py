from .models import Category


def get_categories(request):
    categories = Category.objects.all()
    return {'product_categories': categories}