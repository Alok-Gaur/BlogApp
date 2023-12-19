from django.db import models
from

# Create your models here.
class UserPost(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    timestamp = models.DateTimefield(auto_now=True)
