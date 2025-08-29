from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from django.core.mail import EmailMessage

from blog.models import Post

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/posts.html'
    paginate_by = 5
    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by('-created_at')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog\post.html'

    def get_object(self):
        post = Post.objects.get(pk=self.kwargs['pk'])
        post.views += 1
        post.save()
        if post.views == 100:
            post.send_congratulation_email()
        return post




class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/new_post.html'
    success_url = reverse_lazy('blogs:posts')
    login_url = reverse_lazy('users:login')


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/post_edit.html'
    login_url = reverse_lazy('users:login')

    def get_success_url(self):
        return reverse_lazy('blogs:post', kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blogs:posts')
    login_url = reverse_lazy('users:login')


