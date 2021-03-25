from django.shortcuts import render
# from django.http import HttpResponse  #no longer used since we're using render to display html files

def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')
