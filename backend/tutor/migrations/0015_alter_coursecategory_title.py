# Generated by Django 4.1.2 on 2022-11-08 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0014_course_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecategory',
            name='title',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]