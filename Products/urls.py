from django.urls import path
from .views import (product_list ,
                    product_detail ,
                    search_item ,
                    product_by_category ,
                    Categories_list_partial_view,
                    )
app_name="Products"

urlpatterns = [
    path('product',product_list.as_view(),name="products"),
    path('product/<category_name>/list',product_by_category.as_view(),name="products_by_category"),
    path('product/<id>',product_detail,name="detail"),
    path('product/search/',search_item.as_view(),name="search"),
    path('productCategories_listmmmmmmmmmmmmmmm',Categories_list_partial_view,name="Categories_list"),
    ]
