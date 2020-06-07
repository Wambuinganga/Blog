from django.db import models
from django.contrib.auth.models import User


STATUS=(
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title=models.CharField(max_length=50, unique=True)
    slug=models.SlugField(max_length=100, unique=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    status=models.IntegerField(choices=STATUS, default=0)
    content=models.TextField()



    def __str__(self):
        return self.title




# Create your models here.
