from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from blog.models import Post, PostTag, PostComment
from blog.forms import CommentForm
from user.models import AnonymousUser


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

    return render(request, 'post/index.html', {'posts': posts, 'tags': tags, 'subtitle': tag})


def view(request, slug):
    """
    View a post, images, tags and comments.
    :param request:
    :param slug:
    :return:
    """
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm()

    return render(request, 'post/view.html', {'post': post, 'form': form})


def comment(request, slug):
    """
    Comment on a post.
    :param request:
    :param slug:
    :return:
    """
    try:
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)

        if not form.is_valid():
            return render(request, 'post/view.html', {'post': post, 'form': form})

        try:
            anonymous_user = AnonymousUser.objects.filter(identifier=request.session.session_key).get()
        except AnonymousUser.DoesNotExist:
            anonymous_user = AnonymousUser()
            anonymous_user.identifier = request.session.session_key
            anonymous_user.ip_address = '123.123.123.123'
            anonymous_user.save()

        if not anonymous_user.is_blocked:
            post_comment = PostComment()
            post_comment.name = form.cleaned_data['name']
            post_comment.comment = form.cleaned_data['comment']
            post_comment.anonymous_user = anonymous_user
            post_comment.post = post
            post_comment.save()

        return redirect('view', slug=post.slug)
    except Exception as e:
        print('EXCEPTION ENCOUNTERED')
        print(str(e))
        return HttpResponse(str(e))
