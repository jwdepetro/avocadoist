# Generated by Django 2.2.7 on 2019-12-01 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191201_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=250, null=True, verbose_name='slug'),
        ),
    ]
