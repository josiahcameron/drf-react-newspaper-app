# Generated by Django 4.1.7 on 2023-02-27 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_is_submitted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_submitted',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='new_story',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
