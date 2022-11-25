# Generated by Django 4.1.2 on 2022-11-23 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutor', '0029_certificate_postcertificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userassignment', models.FileField(upload_to='user/assignments')),
                ('assignmentsname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor.assignments')),
                ('chaptername', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor.chapter')),
                ('studentname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tutorname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor.teacher')),
            ],
            options={
                'verbose_name_plural': '6.User Assignments',
            },
        ),
    ]
