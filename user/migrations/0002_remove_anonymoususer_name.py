# Generated by Django 2.2.7 on 2019-12-02 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anonymoususer',
            name='name',
        ),
    ]
