from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import CategoriesTemplateView, ContactListView, ProductListView, ProductDetailView, ProductCreateView, \
    CatalogTemplateView, ProductUpdateView, ProductDeleteView

app_name = 'catalog'

handler404 = views.Custom404View.as_view()

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('categories/', CategoriesTemplateView.as_view(), name='categories'),
    path('catalog/', CatalogTemplateView.as_view(), name='catalog'),
    path('product_details/<int:pk>', ProductDetailView.as_view(), name='product_details'),
    path('edit_product/<int:pk>', ProductUpdateView.as_view(), name='edit_product'),
    path('delete_product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('new_product/', ProductCreateView.as_view(), name='new_product'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)