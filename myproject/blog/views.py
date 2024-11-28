from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from .models import Blog

# Create your views here.
@login_required
def blogform_view(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit = False)
            blog.created_by = request.user
            blog.save()
            return redirect(bloglist_view)

    form = BlogForm()
    context= {"form":form}
    return render(request, 'blog/blogform.html', context)

def editblog_view(request):
    pass


def bloglist_view(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, 'blog/bloglist.html', context)


def deleteblog_view(request):
    pass


def blog_view(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {"blog": blog}

    return render(request, 'blog/blogview.html', context)