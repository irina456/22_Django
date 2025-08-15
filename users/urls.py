from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import RegisterView, LogoutView, ProfileView, ProfileUpdateView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:index'), name='logout'),
    path('register/', RegisterView.as_view(template_name='users/register.html'), name='register'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile_edit/<int:pk>', ProfileUpdateView.as_view(), name='profile_edit'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)