# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,  get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import PostForm

def foo(request):
    return HttpResponse("Hello World!")
def bar(request):
    return HttpResponse("Goodbye Cruel World!")
def hell(request):
    return render(request, 'hello.html', {})
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'hello/post_detail.html', {'post': post})
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'hello/post_edit.html', {'form': form})
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'hello/post_edit.html', {'form': form})
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'hello/post_draft_list.html', {'posts': posts})
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
def publish(self):
    self.published_date = timezone.now()
    self.save()
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
