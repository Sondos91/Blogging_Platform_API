# Generated by Django 5.1.4 on 2024-12-21 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_blog_category_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.blog'),
        ),
    ]