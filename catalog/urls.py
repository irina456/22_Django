from django.urls import path

from catalog.apps import CatalogProjectConfig

from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contacts/', views.contacts_view, name='contacts'),
]