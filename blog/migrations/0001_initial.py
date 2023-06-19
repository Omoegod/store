# Generated by Django 4.2.2 on 2023-06-19 10:56

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('extended_title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.FileField(upload_to='')),
                ('article_block', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.FileField(upload_to='')),
                ('article_block', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_title', models.CharField(blank=True, max_length=200, null=True)),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
                ('article_block', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='article_block',
            field=models.ManyToManyField(blank=True, null=True, to='blog.articleblock'),
        ),
        migrations.AddField(
            model_name='article',
            name='image_block',
            field=models.ManyToManyField(blank=True, null=True, to='blog.photo'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='blog.tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='video_block',
            field=models.ManyToManyField(blank=True, null=True, to='blog.video'),
        ),
    ]
