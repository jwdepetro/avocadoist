# Generated by Django 2.2.7 on 2019-12-02 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(upload_to='images'),
        ),
    ]
