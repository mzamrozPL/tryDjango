# Generated by Django 3.0.5 on 2020-04-09 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200408_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]