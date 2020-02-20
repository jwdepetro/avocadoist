"""
Unit tests for the blog module.
"""

# pylint: disable-msg=E1101

from django.test import TestCase
from faker import Faker
from blog.models import Tag, Post, PostTag, PostComment
from user.tests import create_anonymous_user

FAKER = Faker()


def create_tag(**kwargs) -> Tag:
    """
    Creates a tag
    """
    kwargs.setdefault('name', FAKER.word())
    return Tag.objects.create(**kwargs)


def create_post(**kwargs) -> Post:
    """
    Creates a post
    """
    kwargs.setdefault('title', FAKER.words(2))
    kwargs.setdefault('slug', FAKER.word())
    kwargs.setdefault('body', FAKER.words(200))
    kwargs.setdefault('meta_title', FAKER.words(3))
    kwargs.setdefault('meta_description', FAKER.words(3))
    return Post.objects.create(**kwargs)


def create_post_tag(tag=None, post=None) -> PostTag:
    """
    Creates a post tag
    """
    tag = create_tag() if tag is None else tag
    post = create_post() if post is None else post
    return PostTag.objects.create(tag=tag, post=post)


def create_post_comment(**kwargs) -> PostComment:
    """
    Creates a post comment
    """
    kwargs.setdefault('name', FAKER.name())
    kwargs.setdefault('comment', FAKER.words(10))
    kwargs.setdefault('post', create_post())
    kwargs.setdefault('anonymous_user', create_anonymous_user())
    return PostComment.objects.create(**kwargs)


class TagTestCase(TestCase):
    """
    Test cases for tags
    """

    def test_tag_count(self):
        """
        Tests the tag post count
        """
        tag = create_tag(name='dogs')
        create_post_tag(tag=tag)

        self.assertEqual(tag.post_count(), 1)


class PostTestCase(TestCase):
    """
    Test cases for posts
    """

    def test_comment_count(self):
        """
        Tests the post comment count
        """
        post_comment = create_post_comment()

        self.assertEqual(post_comment.post.comment_count(), 1)

    def test_tags(self):
        """
        Tests the post tag
        """
        post = create_post()
        dogs = create_tag(name='dogs')
        squirrel = create_tag(name='squirrel!')
        cats = create_tag(name='cats')

        create_post_tag(post=post, tag=dogs)
        create_post_tag(post=post, tag=squirrel)
        create_post_tag(post=post, tag=cats)

        # Alphabetical order
        self.assertEqual(post.tags(), 'cats, dogs, squirrel!')


class PostCommentCase(TestCase):
    """
    Test cases for post comments
    """

    def test_post_title(self):
        """
        Tests the comment post title
        """
        post = create_post(title='motley smells bad')
        post_comment = create_post_comment(post=post)

        self.assertEqual(post_comment.post_title(), 'motley smells bad')

    def test_is_user_blocked(self):
        """
        Tests the commented user is blocked and not blocked
        """
        anonymous_user = create_anonymous_user(is_blocked=True)
        post_comment = create_post_comment(anonymous_user=anonymous_user)

        self.assertTrue(post_comment.is_user_blocked())

        anonymous_user = create_anonymous_user(is_blocked=False)
        post_comment = create_post_comment(anonymous_user=anonymous_user)

        self.assertFalse(post_comment.is_user_blocked())
