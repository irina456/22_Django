from django.contrib.auth.mixins import LoginRequiredMixin
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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/new_product.html'
    success_url = reverse_lazy('catalog:index')
    login_url = reverse_lazy('users:login')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/edit_product.html'
    login_url = reverse_lazy('users:login')

    def get_success_url(self):
        return reverse_lazy('catalog:product_details', kwargs={'pk': self.object.pk})

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/delete_product.html'
    success_url = reverse_lazy('catalog:index')
    login_url = reverse_lazy('users:login')

class Custom404View(TemplateView):
    template_name = 'catalog/404.html'

