# Generated by Django 5.0.4 on 2024-04-18 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_order_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='category',
            field=models.IntegerField(choices=[(1, '微博明星'), (2, '微博媒体'), (3, '微博新闻')], default=1, verbose_name='分类'),
        ),
    ]
