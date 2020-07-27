from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

def detail(request, blog_id): # To return the request with a 'detail' page based on the 'blog_id'
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detailblog})