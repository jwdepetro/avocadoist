# Generated by Django 2.2.7 on 2019-12-01 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.FileField(default='image', upload_to='uploads'),
            preserve_default=False,
        ),
    ]
