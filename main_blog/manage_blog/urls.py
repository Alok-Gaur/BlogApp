from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path("/<int:key>", views.blog_page, name="blog_page"),
    path("admin/", views.admin_page, name="admin_page")
]
