# Generated by Django 2.2.2 on 2019-11-25 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='UUID',
            field=models.CharField(max_length=36),
        ),
    ]
