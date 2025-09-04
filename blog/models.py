from django.db import models
from django.urls import reverse
from account.models import Author
# Create your models here.


class Tags(models.Model):
    title = models.CharField(max_length=100, verbose_name='tags name')
    description = models.TextField(verbose_name='explanation')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='category name')
    description = models.TextField(verbose_name='explanation')

    def __str__(self):
        return self.title


class Blogs(models.Model):
    title = models.CharField(max_length=200, verbose_name='the title')
    description = models.CharField(max_length=400, default='something')
    context = models.TextField(verbose_name='blog context')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='time')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tags, related_name='blogstag')
    category = models.ForeignKey(
        Category,
        related_name='blogscat',
        null=True,
        on_delete=models.CASCADE)
    image_file = models.ImageField(
        upload_to='product_images/',
        verbose_name='picture',
        null=True,
        blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[self.pk])


class Comment(models.Model):
    post = models.ForeignKey(
        Blogs,
        on_delete=models.CASCADE,
        related_name="comments")
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="replies",
        on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.content[:20]}"

    @property
    def children(self):
        return self.replies.all()

    def is_parent(self):
        return self.parent is None


class MenuItem(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    url = models.CharField(
        max_length=300,
        verbose_name="link",
        help_text="مثلا /about/ یا یک url کامل")
    order = models.PositiveIntegerField(default=0, verbose_name="ordering ")
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
