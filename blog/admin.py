from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'created_at')
    list_filter = ('created_at', 'is_published',)
    search_fields = ('title', 'content',)