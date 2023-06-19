# Generated by Django 4.2.2 on 2023-06-19 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_block',
        ),
        migrations.RemoveField(
            model_name='article',
            name='image_block',
        ),
        migrations.RemoveField(
            model_name='article',
            name='video_block',
        ),
        migrations.AlterField(
            model_name='articleblock',
            name='article_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='article_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article'),
        ),
        migrations.AlterField(
            model_name='video',
            name='article_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article'),
        ),
    ]