from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Blogs, Comment, Category, Tags
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.db.models import Count
from django.core.paginator import Paginator
# Create your views here.
class BlogsList(ListView):
    model=Blogs
    ordering=['-created_at']
    paginate_by = 2

@method_decorator(login_required,name='dispatch' )
class BlogsCreateView(CreateView):
    model=Blogs
    fields=['title', 'context','image_file','category', 'tag']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogsDetailView(DetailView):
    model=Blogs

@method_decorator(login_required,name='dispatch' )
class BlogsUpdateView(UserPassesTestMixin, UpdateView):
    model=Blogs
    fields=['title', 'context']
    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.author

@method_decorator(login_required, name='dispatch' )
class BlogsDeleteView(UserPassesTestMixin, DeleteView):
    model=Blogs
    success_url=reverse_lazy('post-list')
    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.author

def HomeView(request):
    blogObject = Blogs.objects.all().order_by('-created_at')
    paginator = Paginator(blogObject, 2) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog.html', {'page_obj': page_obj})

## view of partials
def mainHeader(request):
    return render(request,'includes/main-header.html')
def footer(request):
    return render(request,'includes/footer.html')
def sideBar(request):
    posts=Blogs.objects.all().order_by('-created_at')[:3]
    categoryblog=Category.objects.annotate(blog_count=Count('blogscat'))
    tagblog=Tags.objects.annotate(tg_count=Count('blogstag')).order_by('tg_count')
    tagblogs=tagblog[:5]
    return render(request,'includes/side-bar.html',{'catblog':categoryblog, 'tagblogs':tagblogs, 'lastposts':posts})

def blog_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    blogs = Blogs.objects.filter(category=category)
    categories = Category.objects.annotate(post_count=Count('blogscat'))
    return render(request, 'blog/blog_list_category.html', {'blogs': blogs,'categories': categories,'selected_category': category,})


def blogComment(request, pk):
    post = get_object_or_404(Blogs, pk=pk)
    comments = post.comments.filter(parent__isnull=True) 
    if request.method == "POST":
        content = request.POST.get("content")
        parent_id = request.POST.get("parent_id")
        parent_obj = None
        if parent_id:
            parent_obj = Comment.objects.get(id=parent_id)
        Comment.objects.create(
            post=post, user=request.user, content=content, parent=parent_obj
        )
        return redirect("post-detail", pk=pk)

    return render(request, "includes/comments.html", {"post": post, "comments": comments})