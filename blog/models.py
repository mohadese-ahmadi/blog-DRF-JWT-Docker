from django.db import models
from account.models import Author
# Create your models here.
class Tags(models.Model):
    title=models.CharField(max_length=100, verbose_name='tags name')
    description=models.TextField(verbose_name='explanation')
    def __str__(self):
        return self.title
class Category(models.Model):
    title=models.CharField(max_length=200 ,  verbose_name='category name')
    description=models.TextField(verbose_name='explanation')
    def __str__(self):
        return self.title
class Blogs(models.Model):
    title=models.CharField(max_length=200, verbose_name='the title')
    context=models.TextField(verbose_name='blog context')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='time')
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    tag=models.ManyToManyField(Tags, related_name='blogstag')
    category=models.ForeignKey( Category, related_name='blogscat' ,null=True, on_delete=models.CASCADE)
    image_file=models.ImageField(upload_to='product_images/', verbose_name='picture', null=True, blank=True)
    def __str__(self):
        return self.title
