from django.shortcuts import render
from .models import UserPost
# Create your views here.

def index(request):
    blog_posts = UserPost.objects.all().order_by('timestamp')
    return render(request, 'index.html', {'blog_posts': blog_posts})


def blog_page(request, key):
    blog_post = UserPost.objects.get(id = key)
    return render(request, 'blog-page.html', {'blog_post': blog_post})


def admin_page(request):
    if request.method == 'POST':
        # this checks for which form user submitted
        if request.POST.get('form_type') == 'create':
            title = request.POST['title']
            content = request.POST['input-content']
            UserPost.objects.create(title=title, content=content)
        
        else:
            id = request.POST['blog_id']
            post = UserPost.objects.get(id=id)
            post.delete()

    blog_posts = UserPost.objects.all().order_by('timestamp')
    return render(request, 'admin-page.html', {'blog_posts': blog_posts})