from django.contrib import admin

# Register your models here.

from .models import Post

#to register our Post model
admin.site.register(Post)