# Generated by Django 2.2.7 on 2019-12-02 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191201_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='name',
            field=models.CharField(max_length=30, verbose_name='name'),
            preserve_default=False,
        ),
    ]
