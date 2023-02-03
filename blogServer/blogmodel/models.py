from django.db import models

class Post(models.Model):
    blogTitle=models.CharField(max_length=255)
    blogContent=models.TextField()


