# Generated by Django 4.0.2 on 2022-04-26 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_student_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='classroom',
        ),
    ]
