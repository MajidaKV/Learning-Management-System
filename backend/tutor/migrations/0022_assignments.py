# Generated by Django 4.1.2 on 2022-11-09 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0021_rename_is_addded_coursecategory_is_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('assignment_file', models.FileField(blank=True, upload_to='assignment/chapter/')),
                ('is_done', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor.course')),
            ],
        ),
    ]
