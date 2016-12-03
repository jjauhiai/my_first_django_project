# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.utils import timezone

def foo(request):
    return HttpResponse("Hello World!")
def bar(request):
    return HttpResponse("Goodbye Cruel World!")
def hell(request):
    return render(request, 'hello.html', {})
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})
