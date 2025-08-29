from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail
from django.urls import  reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from .models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    template_name='users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        send_mail(
            subject="Регистрация на сайте",
            message="Здравствуйте! Вы зарегистрировались на сайте.",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('catalog:index')

class ProfileView(TemplateView):
    template_name = 'users/profile.html'

class ProfileUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'pk': self.object.pk})
    template_name = 'users/profile_edit.html'