from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blog.models import Blogs, Tags, Category
from .serializers import BlogSerializer, TagSerializer, CategorySerializer, RegisterSerializer
from account.models import Author
from rest_framework import generics
from rest_framework.permissions import AllowAny
# Create your views here.

class BlogViewSets(viewsets.ModelViewSet):
    queryset=Blogs.objects.all().order_by('created_at')
    serializer_class=BlogSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    def perform_create(self,serializer):
        serializer.save(author=self.request.user)
class TagViewSets(viewsets.ModelViewSet):
    queryset=Tags.objects.all()
    serializer_class=TagSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class RegisterView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]