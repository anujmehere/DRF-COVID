# Generated by Django 3.2 on 2021-04-28 18:42

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='posts/default.JPG', upload_to=blog.models.upload_to, verbose_name='Image'),
        ),
    ]
