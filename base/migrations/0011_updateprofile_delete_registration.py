# Generated by Django 4.0.4 on 2022-08-25 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0010_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProfilePic', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField(max_length=1000)),
                ('skills', models.CharField(choices=[('webdevelopment', 'webdevelopment'), ('DSA', 'DSA'), ('Android development', 'Android development'), ('Compitative programming', 'Compitative programming'), ('AWS', 'AWS')], max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
