from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {
        'posts':posts,
    })

def show(request, pk):
    # post = Post.objects.get(pk=pk)

    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/show.html', {
        'post':post,
    })

def new():
    pass

def exit():
    pass

def delete():
    pass