from django.urls import path

from .views import PostListView, PostDetailView

from . import views		# . means current directory

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),#pk->primary key(int:integer)
    path('about/', views.about, name='blog-about'),
]
