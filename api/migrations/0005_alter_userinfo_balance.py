# Generated by Django 5.0.4 on 2024-04-18 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_userinfo_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='balance',
            field=models.IntegerField(blank=True, null=True, verbose_name='余额'),
        ),
    ]
