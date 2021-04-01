from django.shortcuts import render
# from django.http import HttpResponse  #no longer used since we're using render to display html files

from .models import Post    # .models as model in same directory

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )

#to require login when creating a post, allow only user who created the post to update the post 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



# dummy test data
# posts = [
#     {
#         'author': 'person1',
#         'title': 'blog post1',
#         'content': 'First post',
#         'date_posted': '25/3/21'
#     },
#     {
#         'author': 'person2',
#         'title': 'blog post2',
#         'content': 'Second post',
#         'date_posted': '25/3/21'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'    # <app>/<model>_<viewtype>.html

    context_object_name = 'posts'
    #order post by newest to oldest
    ordering = ['-date_posted']     #the "-" sign causes the newest to oldest
    paginate_by = 7


class PostDetailView(DetailView):
    model = Post


#login required to create post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user#setup post author as current logged in user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user#setup post author as current logged in user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        #if current user is post author, then only allow post update
        if self.request.user == post.author:
            return True
        #else
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    #if deleted, redirect to home page
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        #if current user is post author, then only allow post update
        if self.request.user == post.author:
            return True
        #else
        return False



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
