# Generated by Django 4.1.2 on 2022-10-25 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0006_teachertoken'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teachertoken',
            old_name='teacher_id',
            new_name='tutor_id',
        ),
    ]
