# Generated by Django 4.0.4 on 2022-08-25 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_delete_followerscount_delete_likepost_post_updated_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('school_email', models.EmailField(max_length=254)),
                ('set_password', models.CharField(max_length=1000)),
                ('confirm_password', models.CharField(max_length=1000)),
                ('Identity', models.ImageField(upload_to='')),
            ],
        ),
    ]
