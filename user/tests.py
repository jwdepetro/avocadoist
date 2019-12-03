from django.test import TestCase
from faker import Faker
from user.models import AnonymousUser

fake = Faker()


def create_anonymous_user(**kwargs) -> AnonymousUser:
    kwargs.setdefault('identifier', fake.uuid4())
    kwargs.setdefault('ip_address', fake.ipv4())
    kwargs.setdefault('is_blocked', False)
    return AnonymousUser.objects.create(**kwargs)
