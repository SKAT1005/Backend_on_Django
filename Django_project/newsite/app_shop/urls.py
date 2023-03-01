from django.urls import path

from .views import HomePage, Catalog, CatalogFilter, CatalogFilterTeg, FilterPriceAndPopular, detail_prod, \
    FilterCategoryView, add_prod_in_cart, select_category, remove_prod_form_cart

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('catalog/', Catalog.as_view(), name='catalog'),
    path('catalog/filter/<str:pk>', CatalogFilter.as_view(), name='catalog_filter'),
    path('catalog/teg/<int:pk>', CatalogFilterTeg.as_view(), name='catalog_filter_teg'),
    path('catalog/category/<int:pk>', FilterCategoryView.as_view(), name='catalog_filter_category'),
    path('catalog/filter/price/<int:pk>', FilterPriceAndPopular.as_view(), name='catalog_filter_price_popular'),
    path('catalog/prod/<int:pk>', detail_prod, name='detail_prod'),
    path('catalog/prod/add_in_cart/<int:pk>', add_prod_in_cart, name='add_prod_in_cart'),
    path('catalog/prod/remove_from_cart/<int:pk>', remove_prod_form_cart, name='remove_from_cart'),
    path('select_category/<int:pk>', select_category, name='select_category')
]
