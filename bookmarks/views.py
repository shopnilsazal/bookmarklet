from django.shortcuts import render, redirect
from bookmarks.models import Category, Page
from .forms import CategoryForm, PageForm, UserForm, UserProfileForm

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


def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(index)
        else:
            print(form.errors)

    context = {
        'form': form
    }
    return render(request, 'add_category.html', context)


def add_page(request, category_slug):
    try:
        category = Category.objects.get(slug=category_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return redirect(show_category, category_slug)
        else:
            print(form.errors)

    context = {
        'form': form,
        'category': category
    }

    return render(request, 'add_page.html', context)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }

    return render(request, 'register.html', context)
