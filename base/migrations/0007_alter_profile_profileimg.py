# Generated by Django 4.0.4 on 2022-08-18 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_followerscount_likepost_post_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(upload_to='profile_images'),
        ),
    ]
