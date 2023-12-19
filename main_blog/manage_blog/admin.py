from django.contrib import admin
from .models import UserPost
from django.utils.text import Truncator

# Register your models here.
class UserPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_short_content')

    def display_short_content(self, obj):
        return Truncator(obj.content).words(16, html=True)
    display_short_content.short_discription = 'content'
admin.site.register(UserPost, UserPostAdmin)