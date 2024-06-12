# Generated by Django 5.0.4 on 2024-04-18 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='category',
            field=models.IntegerField(blank=True, choices=[(1, '微博明星'), (2, '微博媒体'), (3, '微博新闻')], null=True, verbose_name='分类'),
        ),
    ]
