# Generated by Django 4.1.1 on 2022-10-11 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_alter_pet_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='type',
            field=models.CharField(default='pet', max_length=30),
        ),
    ]
