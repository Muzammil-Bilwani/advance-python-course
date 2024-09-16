from django.urls import path
from . import views

urlpatterns = [
    path('split-evenly/', view=views.split_evenly,
         name='split-evenly'),

    path('split-unevenly/', view=views.split_unevenly,
         name='split-unevenly'),

    path('split-including-tip-tax/', view=views.split_including_tip_tax,
         name='split-including-tip-tax'),

    path('split-with-discount/', view=views.split_with_discount,
         name='split-with-discount'),

    path('split-with-shared-items/', view=views.split_with_shared_items,
         name='split-with-shared-items'),
]
