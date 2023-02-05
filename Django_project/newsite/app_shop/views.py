from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from app_users.models import Profile
from .forms import FilterForm, ReviewsForm
from .models import Product, Category, Reviews, Tegs


class HomePage(View):
    """Представление главной страницы"""

    def get(self, request):
        category = Category.objects.all()
        profile = Profile.objects.get(id=request.user.id)
        sell_cat = profile.selected_category.all()[:3]
        popular_prod = Product.objects.order_by('reviews')[:8]
        limited_prod = Product.objects.filter(limited_edition=True)[:16]
        return render(request, 'registration/index.html', context={'sell_cat': sell_cat,
                                                                   'popular_prod': popular_prod,
                                                                   'limited_prod': limited_prod,
                                                                   'category': category})


class Catalog(View):
    """Представление каталога"""

    def get(self, request):
        category = Category.objects.all()
        prod = Product.objects.all()
        filter_form = FilterForm
        tegs = Tegs.objects.all()
        return render(request, 'registration/catalog.html', context={'category': category,
                                                                     'prod': prod,
                                                                     'filter_form': filter_form,
                                                                     'tegs': tegs})

    def post(self, request):
        filter_form = FilterForm(request.POST)
        if filter_form.is_valid():
            filtet = filter_form.cleaned_data.get('name')
            return HttpResponseRedirect(f'http://127.0.0.1:8000/prod/catalog/filter/{filtet}')
        else:
            category = Category.objects.all()
            prod = Product.objects.all()
            filter_form = FilterForm
            tegs = Tegs.objects.all()
            return render(request, 'registration/catalog.html', context={'category': category,
                                                                         'prod': prod,
                                                                         'filter_form': filter_form,
                                                                         'tegs': tegs})


class CatalogFilter(View):
    """Представление каталога с фильтром по имени"""

    def get(self, request, pk):
        category = Category.objects.all()
        prod = Product.objects.filter(name=pk)
        filter_form = FilterForm
        tegs = Tegs.objects.all()
        return render(request, 'registration/catalog.html', context={'category': category,
                                                                     'prod': prod,
                                                                     'filter_form': filter_form,
                                                                     'tegs': tegs})

    def post(self, request, pk):
        filter_form = FilterForm(request.POST)
        tegs = Tegs.objects.all()
        if filter_form.is_valid():
            filtet = filter_form.cleaned_data.get('name')
            return HttpResponseRedirect(f'http://127.0.0.1:8000/prod/catalog/filter/{filtet}')
        else:
            category = Category.objects.all()
            prod = Product.objects.filter(name=pk)
            return render(request, 'registration/catalog.html', context={'category': category,
                                                                         'prod': prod,
                                                                         'filter_form': filter_form,
                                                                         'tegs': tegs})


class CatalogFilterTeg(View):
    """Представление фильтра по тегу"""

    def get(self, request, pk):
        tegs = Tegs.objects.all()
        category = Category.objects.all()
        filter_tegs = Tegs.objects.get(id=pk)
        prod = Product.objects.filter(tegs=filter_tegs)
        filter_form = FilterForm
        return render(request, 'registration/catalog.html', context={'category': category,
                                                                     'prod': prod,
                                                                     'filter_form': filter_form,
                                                                     'tegs': tegs})

    def post(self, request, pk):
        tegs = Tegs.objects.all()
        filter_form = FilterForm(request.POST)
        if filter_form.is_valid():
            filtet = filter_form.cleaned_data.get('name')
            return HttpResponseRedirect(f'http://127.0.0.1:8000/prod/catalog/filter/{filtet}')
        else:
            category = Category.objects.all()
            filter_tegs = Tegs.objects.get(id=pk)
            prod = Product.objects.filter(tegs=filter_tegs)
            return render(request, 'registration/catalog.html', context={'category': category,
                                                                         'prod': prod,
                                                                         'filter_form': filter_form,
                                                                         'tegs': tegs})


class FilterCategoryView(View):
    """Представление фильтра по категориям"""

    def get(self, request, pk):
        tegs = Tegs.objects.all()
        category = Category.objects.all()
        filter_category = Category.objects.get(id=pk)
        prod = Product.objects.filter(category=filter_category)
        filter_form = FilterForm
        return render(request, 'registration/catalog.html', context={'category': category,
                                                                     'prod': prod,
                                                                     'filter_form': filter_form,
                                                                     'tegs': tegs})

    def post(self, request, pk):
        tegs = Tegs.objects.all()
        filter_form = FilterForm(request.POST)
        if filter_form.is_valid():
            filtet = filter_form.cleaned_data.get('name')
            return HttpResponseRedirect(f'http://127.0.0.1:8000/prod/catalog/filter/{filtet}')
        else:
            category = Category.objects.all()
            filter_category = Category.objects.get(id=pk)
            prod = Product.objects.filter(tegs=filter_category)
            return render(request, 'registration/catalog.html', context={'category': category,
                                                                         'prod': prod,
                                                                         'filter_form': filter_form,
                                                                         'tegs': tegs})


class FilterPriceAndPopular(View):
    """Представление фильтрации по цене и популярности"""

    def get(self, request, pk):
        tegs = Tegs.objects.all()
        category = Category.objects.all()
        if pk == 1:
            print(1)
            prod = Product.objects.order_by("price")
        elif pk == 2:
            print(2)
            prod = Product.objects.order_by("-price")
        elif pk == 3:
            print(3)
            prod = Product.objects.order_by("reviews_count")
        else:
            print(4)
            prod = Product.objects.order_by("-reviews_count")
        filter_form = FilterForm
        return render(request, 'registration/catalog.html', context={'category': category,
                                                                     'prod': prod,
                                                                     'filter_form': filter_form,
                                                                     'tegs': tegs})

    def post(self, request, pk):
        tegs = Tegs.objects.all()
        filter_form = FilterForm(request.POST)
        if filter_form.is_valid():
            filter = filter_form.cleaned_data.get('description')
            return HttpResponseRedirect(f'http://127.0.0.1:8000//prodcatalog/filter/{filter}')
        else:
            category = Category.objects.all()
            if pk == 1:
                prod = Product.objects.order_by("price")
            elif pk == 2:
                prod = Product.objects.order_by("-price")
            elif pk == 3:
                prod = Product.objects.order_by("count")
            else:
                prod = Product.objects.order_by("-count")
        return render(request, 'registration/catalog.html', context={'category': category,
                                                                     'prod': prod,
                                                                     'filter_form': filter_form,
                                                                     'tegs': tegs})


def detail_prod(request, pk):
    """Представление детали товара"""
    form = ReviewsForm(request.POST)
    category = Category.objects.all()
    prod = Product.objects.get(id=pk)
    profile = Profile.objects.get(id=request.user.id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if form.is_valid():
                reviews = Reviews.objects.create(
                    user_name=request.user.first_name,
                    avatar=profile.avatar,
                    text=form.cleaned_data.get('text')
                )
                reviews.save()
                prod.reviews.add(reviews)
                prod.reviews_count += 1
            else:
                form = ReviewsForm()
        else:
            return HttpResponseRedirect('http://127.0.0.1:8000/login/')
    return render(request, 'registration/product.html', {'form': form,
                                                         'category': category,
                                                         'prod': prod, })


def add_prod_in_cart(request, pk):
    """Добавление товара в корзину"""
    profile = Profile.objects.get(id=request.user.id)
    prod = Product.objects.get(id=pk)
    profile.cart.add(prod)
    profile.save()
    return HttpResponseRedirect('http://127.0.0.1:8000/prod/catalog/')


def remove_prod_form_cart(request, pk):
    """Удаление товара из корзины"""
    prod = Product.objects.get(id=pk)
    profile = Profile.objects.get(id=request.user.id)
    profile.cart.remove(prod)
    profile.save()
    return HttpResponseRedirect('http://127.0.0.1:8000/profile/cart')


def select_category(request, pk):
    """Добавление категории в избранное"""
    category = Category.objects.get(id=pk)
    profile = Profile.objects.get(id=request.user.id)
    profile.selected_category.add(category)
    return HttpResponseRedirect('http://127.0.0.1:8000/prod/catalog/')
