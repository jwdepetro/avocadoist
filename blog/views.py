from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from blog.models import Post, PostTag


def index(request):
    """
    Get all recent posts for the home page.
    :param request:
    :return:
    """
    page = request.GET.get('page', 1)
    tag = request.GET.get('tag', None)

    if tag:
        post_list = Post.objects.filter(post_tags__tag__name=tag)
    else:
        post_list = Post.objects.all()

    post_list = post_list.order_by('-created_at')
    paginator = Paginator(post_list, 50)
    posts = paginator.get_page(page)
    tags = PostTag.objects.values('tag__name').annotate(count=Count('tag')).order_by('-count')

    return render(request, 'post/index.html', {
        'posts': posts,
        'tags': tags
    })


def view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'post/view.html', {
        'post': post
    })
