from django.shortcuts import render
from .models import Post
# from django.http import Http404
from django.shortcuts import get_object_or_404

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(requset, id):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("Постов нету")
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(requset, 'blog/post/detail.html', {'post': post})

