# Generated by Django 4.1.2 on 2022-11-24 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_totalmarks_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='Quiz',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='marks',
            name='question_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='marks',
            name='mark',
            field=models.IntegerField(null=True),
        ),
    ]
