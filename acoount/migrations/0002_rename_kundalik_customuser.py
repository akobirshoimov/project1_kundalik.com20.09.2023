# Generated by Django 4.2.5 on 2023-09-20 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('acoount', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Kundalik',
            new_name='CustomUser',
        ),
    ]
