# Generated by Django 2.2.12 on 2022-05-02 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20220501_2058'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='choices',
            new_name='choice',
        ),
    ]
