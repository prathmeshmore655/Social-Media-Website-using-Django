# Generated by Django 4.2.13 on 2024-07-01 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_comments_commment_by_alter_comments_post_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='commment_By',
            new_name='comment_By',
        ),
    ]
