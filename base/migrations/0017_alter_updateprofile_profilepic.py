# Generated by Django 4.0.4 on 2022-08-27 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_rename_username_updateprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateprofile',
            name='ProfilePic',
            field=models.ImageField(default='default.jpg', null=True, upload_to='profile_images'),
        ),
    ]