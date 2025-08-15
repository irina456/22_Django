from django.contrib import admin

from catalog.models import Category, Product, Contact

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name', 'description',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'git')
    list_filter = ('name', 'last_name',)
    search_fields = ('name', 'last_name', 'email', 'git')