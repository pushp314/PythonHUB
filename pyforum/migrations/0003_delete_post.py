# Generated by Django 4.2.6 on 2024-12-04 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyforum', '0002_remove_comment_author_remove_comment_post_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
