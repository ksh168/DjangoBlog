from django.shortcuts import render
# from django.http import HttpResponse  #no longer used since we're using render to display html files

from .models import Post    # .models as model in same directory

from django.views.generic import (
    ListView,
    DetailView,
    CreateView
    )

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


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
