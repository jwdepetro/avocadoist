"""
Unit tests for the user module.
"""

# pylint: disable-msg=E1101

from faker import Faker
from user.models import AnonymousUser

FAKER = Faker()


def create_anonymous_user(**kwargs) -> AnonymousUser:
    """
    Creates an anonymous user
    """
    kwargs.setdefault('identifier', FAKER.uuid4())
    kwargs.setdefault('ip_address', FAKER.ipv4())
    kwargs.setdefault('is_blocked', False)
    return AnonymousUser.objects.create(**kwargs)
