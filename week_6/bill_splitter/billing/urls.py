from django.urls import path
from . import views

urlpatterns = [
    path('split-with-shared-items/', view=views.splitWIthSharedItems,
         name='split-with-shared-items'),
]
