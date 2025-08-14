from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, ListView, DeleteView, UpdateView
from .forms import ProductForm
from catalog.models import Product, Contact, Category


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products_list'
    paginate_by = 6


class ContactListView(ListView):
    template_name = 'catalog/contacts.html'
    model = Contact
    context_object_name = 'contacts'


class CategoriesTemplateView(TemplateView):
    template_name = 'catalog/categories.html'
    model = Category


class CatalogTemplateView(TemplateView):
    template_name = 'catalog/catalog.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_details.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/new_product.html'
    success_url = reverse_lazy('catalog:index')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/edit_product.html'

    def get_success_url(self):
        return reverse_lazy('catalog:product_details', kwargs={'pk': self.object.pk})

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/delete_product.html'
    success_url = reverse_lazy('catalog:index')


