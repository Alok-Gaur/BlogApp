from django.db import models


# Create your models here.
class UserPost(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
