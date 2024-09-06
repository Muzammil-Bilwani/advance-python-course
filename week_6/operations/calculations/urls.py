from django.urls import path
from .views import *

urlpatterns = [
    path('sum', sum_view, name='sum_view'),
    path('average', average_view, name='average_view'),
    path('product', product_view, name='product_view'),
    path('split-evenly', split_evenly, name='split_evenly'),
    path('split-unevenly',split_unevenly, name='split_unevenly'),
    path('split-evenly-with-tax-tip',split_evenly_with_tax_tip, name='split_evenly_with_tax_tip'),
    path('split-evenly-with-discount', split_evenly_with_discount, name='split_evenly_with_discount')
]