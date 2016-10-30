from django.shortcuts import render
from bookmarks.models import Category, Page

# Create your views here.


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context = {
        'categories': category_list,
        'pages': page_list
    }
    return render(request, 'index.html', context)


def show_category(request, category_slug):
    context = {}

    try:
        category = Category.objects.get(slug=category_slug)
        pages = Page.objects.filter(category=category)
        context['category'] = category
        context['pages'] = pages
    except Category.DoesNotExist:
        context['category'] = None
        context['pages'] = None

    return render(request, 'category.html', context)
