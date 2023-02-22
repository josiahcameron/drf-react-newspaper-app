# Generated by Django 4.1.7 on 2023-02-22 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='new_story',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]