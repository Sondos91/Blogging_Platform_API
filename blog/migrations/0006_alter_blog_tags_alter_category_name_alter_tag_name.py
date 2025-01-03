# Generated by Django 5.1.4 on 2024-12-24 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_tag_blog_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Tags',
            field=models.ManyToManyField(blank=True, related_name='blogs', to='blog.tag'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
