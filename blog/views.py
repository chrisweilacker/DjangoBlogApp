from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    postList = {'posts': posts}
    return render(request, 'blog/post_list.html', postList)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    aPost = {'post': post}
    return render(request, 'blog/post_detail.html', aPost)

def post_detail_by_title(request, title):
    post = get_object_or_404(Post, title=title)
    aPost = {'post': post}
    return render(request, 'blog/post_detail.html', aPost)
