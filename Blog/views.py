from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm
from .models import Post, Project

def about(request):
    return render(request, 'Blog/about.html', {'title': 'About Me', 'color': '#ccf486'})

def archive(request):
    return render(request, 'Blog/archive.html', {'title': 'Blog Archive', 'color': '#ffa189'})

def contact(request):
    return render(request, 'Blog/contact.html', {'title': 'Contact Info', 'color': '#f9f568'})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    return render(request, 'Blog/post_list.html', {'posts': posts, 'title': 'Recent Blog Posts', 'color': '#a3f4ff'})

def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'Blog/post_detail.html', {'post': post, 'title': post.title, 'color': '#a3f4ff'})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'Blog/post_edit.html', {'form': form, 'header': 'New Post'})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'Blog/post_edit.html', {'form': form, 'header': 'Edit Post'})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'Blog/project_list.html', {'projects': projects, 'title': "Projects", 'color': '#d7a0ff'})
