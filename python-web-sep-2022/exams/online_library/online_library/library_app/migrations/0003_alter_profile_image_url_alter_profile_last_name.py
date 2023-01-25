# Generated by Django 4.1.2 on 2022-10-26 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_alter_profile_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image_url',
            field=models.URLField(verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Last Name'),
        ),
    ]