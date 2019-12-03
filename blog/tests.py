from django.test import TestCase
from faker import Faker
from blog.models import Tag, Post, PostTag, PostComment
from user.tests import create_anonymous_user

fake = Faker()


def create_tag(**kwargs) -> Tag:
    kwargs.setdefault('name', fake.word())
    return Tag.objects.create(**kwargs)


def create_post(**kwargs) -> Post:
    kwargs.setdefault('title', fake.words(2))
    kwargs.setdefault('slug', fake.word())
    kwargs.setdefault('body', fake.words(200))
    kwargs.setdefault('meta_title', fake.words(3))
    kwargs.setdefault('meta_description', fake.words(3))
    return Post.objects.create(**kwargs)


def create_post_tag(tag=None, post=None) -> PostTag:
    tag = create_tag() if tag is None else tag
    post = create_post() if post is None else post
    return PostTag.objects.create(tag=tag, post=post)


def create_post_comment(**kwargs) -> PostComment:
    kwargs.setdefault('name', fake.name())
    kwargs.setdefault('comment', fake.words(10))
    kwargs.setdefault('post', create_post())
    kwargs.setdefault('anonymous_user', create_anonymous_user())
    return PostComment.objects.create(**kwargs)


class TagTestCase(TestCase):

    def test_tag_count(self):
        tag = create_tag(name='dogs')
        create_post_tag(tag=tag)

        self.assertEquals(tag.post_count(), 1)


class PostTestCase(TestCase):

    def test_comment_count(self):
        post_comment = create_post_comment()

        self.assertEquals(post_comment.post.comment_count(), 1)

    def test_tags(self):
        post = create_post()
        dogs = create_tag(name='dogs')
        squirrel = create_tag(name='squirrel!')
        cats = create_tag(name='cats')

        create_post_tag(post=post, tag=dogs)
        create_post_tag(post=post, tag=squirrel)
        create_post_tag(post=post, tag=cats)

        # Alphabetical order
        self.assertEquals(post.tags(), 'cats, dogs, squirrel!')


class PostCommentCase(TestCase):

    def test_post_title(self):
        post = create_post(title='motley smells bad')
        post_comment = create_post_comment(post=post)

        self.assertEquals(post_comment.post_title(), 'motley smells bad')

    def test_is_user_blocked(self):
        anonymous_user = create_anonymous_user(is_blocked=True)
        post_comment = create_post_comment(anonymous_user=anonymous_user)

        self.assertTrue(post_comment.is_user_blocked())

        anonymous_user = create_anonymous_user(is_blocked=False)
        post_comment = create_post_comment(anonymous_user=anonymous_user)

        self.assertFalse(post_comment.is_user_blocked())
