from django.shortcuts import render
# from django.http import HttpResponse  #no longer used since we're using render to display html files

posts = [
    {
        'author': 'person1',
        'title': 'blog post1',
        'content': 'First post',
        'date_posted': '25/3/21'
    },
    {
        'author': 'person2',
        'title': 'blog post2',
        'content': 'Second post',
        'date_posted': '25/3/21'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
