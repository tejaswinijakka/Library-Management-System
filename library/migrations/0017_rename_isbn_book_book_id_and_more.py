# Generated by Django 4.0.2 on 2022-04-26 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_remove_student_classroom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='isbn',
            new_name='book_id',
        ),
        migrations.RenameField(
            model_name='issuedbook',
            old_name='isbn',
            new_name='book_id',
        ),
    ]