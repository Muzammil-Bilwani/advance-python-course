from django.urls import path
from .views import *

urlpatterns = [
    path('sum', sum_view, name='sum_view'),
    path('average', average_view, name='average_view'),
    path('product', product_view, name='product_view'),
]