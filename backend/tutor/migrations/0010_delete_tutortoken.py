# Generated by Django 4.1.2 on 2022-10-27 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0009_course_image_course_technology_teacher_dp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TutorToken',
        ),
    ]
