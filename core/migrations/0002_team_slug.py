# Generated by Django 4.1.3 on 2022-11-14 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
