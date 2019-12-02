# Generated by Django 2.2.7 on 2019-12-02 02:54

from django.db import migrations, transaction

SOCIAL_PROFILES = [
    {
        'name': 'Avocadoist',
        'type': 'instagram',
        'link': 'https://www.instagram.com/the_avocadoist',
        'weight': 0
    },
    {
        'name': 'Personal',
        'type': 'instagram',
        'link': 'https://www.instagram.com/carlirae__',
        'weight': 1
    },
    {
        'name': 'Business',
        'type': 'linkedin',
        'link': 'https://www.linkedin.com/in/carli-auran-7a884834/',
        'weight': 2
    },
]


def add_social_profiles(apps, schema_editor):
    SocialProfile = apps.get_model('social', 'SocialProfile')
    SocialType = apps.get_model('social', 'SocialType')

    social_profiles = []

    for item in SOCIAL_PROFILES:
        social_type = SocialType.objects.filter(name=item['type']).get()
        del item['type']
        social_profile = SocialProfile(**item)
        social_profile.social_type = social_type
        social_profiles.append(social_profile)

    with transaction.atomic():
        SocialProfile.objects.bulk_create(social_profiles)


def delete_social_profiles(apps, schema_editor):
    SocialProfile = apps.get_model('social', 'SocialProfile')
    SocialProfile.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('social', '0003_auto_20191202_0253'),
    ]

    operations = [
        migrations.RunPython(add_social_profiles, delete_social_profiles)
    ]
