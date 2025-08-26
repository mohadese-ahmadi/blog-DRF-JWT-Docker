from django.shortcuts import render
from .models import Blogs
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
# Create your views here.
class BlogsList(ListView):
    model=Blogs
class BlogsCreateView(CreateView):
    model=Blogs
class BlogsDetailView(DetailView):
    model=Blogs

class BlogsUpdateView(UpdateView):
    models=Blogs
    fields=['title', 'context']

class BlogsDeleteView(DeleteView):
    models=Blogs
    success_url=reverse_lazy('post-list')

def HomeView(request):
    return render(request, 'blog/blog.html')

## view of partials
def mainHeader(request):
    return render(request,'includes/main-header.html')
def footer(request):
    return render(request,'includes/footer.html')
def sideBar(request):
    return render(request,'includes/side-bar.html')