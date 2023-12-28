from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index_page'),
    path('<slug:category_slug>', category_view, name="category_page"),
    path('AddProduct/', addproduct_view, name='addproduct_page'),
    path('delete/<slug:product_slug>/', delete_view, name='deleteproduct_page'),
    path('bag/', bag_view, name='bag_page'),
    path('AddtoBag/', add_to_bag_view, name='add_page'),
    path('remove_from_bag/<int:bag_item_id>/', remove_from_bag_view, name='remove_from_bag')
]
