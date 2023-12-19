from django.shortcuts import render
from .models import UserPost
# Create your views here.

def index(request):
    blog_posts = UserPost.objects.all()[::-1]
    return render(request, 'index.html', {'blog_posts': blog_posts})


def blog_page(request, key):
    blog_post = UserPost.objects.all().filter(id=key)
    return render(request, 'blog-page.html', {'blog_post': blog_post})