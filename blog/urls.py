from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView

app_name = 'blogs'

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('new_post/', PostCreateView.as_view(), name='new_post'),
    path('post_edit/<int:pk>', PostUpdateView.as_view(), name='post_edit'),
    path('post_delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)