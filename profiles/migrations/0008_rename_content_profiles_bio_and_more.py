# Generated by Django 4.2.11 on 2024-03-24 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_alter_profiles_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiles',
            old_name='content',
            new_name='bio',
        ),
        migrations.RenameField(
            model_name='profiles',
            old_name='title',
            new_name='journal_title',
        ),
    ]