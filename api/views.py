from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from blog.models import Blogs, Tags, Category, Comment
from account.models import Author
from .serializers import (
    BlogSerializer,
    TagSerializer,
    CategorySerializer,
    RegisterSerializer,
    CommentSerializer,
    AuthorSerializer,
)
from .permissions import IsAuthorOrReadOnly, IsSuperUserOrReadOnly


class BlogViewSets(viewsets.ModelViewSet):
    queryset = Blogs.objects.all().order_by("created_at")
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TagViewSets(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RegisterView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get("post_pk")
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_pk")
        serializer.save(post_id=post_id, user=self.request.user)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsSuperUserOrReadOnly]
