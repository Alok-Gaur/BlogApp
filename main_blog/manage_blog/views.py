from django.shortcuts import render
from .models import UserPost
# Create your views here.

def index(request):
    blog_posts = UserPost.objects.all()[::-1]
    return render(request, 'index.html', {'blog_posts': blog_posts})