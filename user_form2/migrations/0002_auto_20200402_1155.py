# Generated by Django 3.0.4 on 2020-04-02 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_form2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='picture',
            new_name='profile_pics',
        ),
    ]
