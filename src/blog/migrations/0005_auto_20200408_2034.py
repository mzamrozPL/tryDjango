# Generated by Django 3.0.5 on 2020-04-08 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200407_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.TextField(max_length=120),
        ),
    ]