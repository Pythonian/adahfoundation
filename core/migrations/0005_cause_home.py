# Generated by Django 4.1.3 on 2022-11-15 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_about_cause_homepage_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='cause',
            name='home',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.homepage'),
            preserve_default=False,
        ),
    ]
