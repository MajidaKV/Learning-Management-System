# Generated by Django 4.1.2 on 2022-11-08 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0018_alter_chapter_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='title',
            new_name='heading',
        ),
    ]
