# Generated by Django 2.2.2 on 2019-11-25 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20191125_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='StripePaymentID',
            field=models.CharField(default='eiwie', max_length=500),
            preserve_default=False,
        ),
    ]