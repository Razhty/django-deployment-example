# Generated by Django 3.2.3 on 2021-06-07 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='username',
            new_name='user',
        ),
    ]
