from django.db import models
# Create your models here.

from django.contrib.auth.models import User
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    image = models.ImageField(blank=True,null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True,null=True, allow_unicode=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True,)
    content =models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    time_for_reading = models.CharField(max_length=2,null=True)
    status = models.BooleanField(default=False)

    views = models.IntegerField(default=1)


    def __str__(self):
        return self.title + " " + self.author