# Generated by Django 4.1 on 2022-09-19 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comic', '0030_comiccomment_alter_chapter_createat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='CreateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 14, 19, 34, 449956)),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='UpdateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 14, 19, 34, 449956)),
        ),
        migrations.AlterField(
            model_name='comic',
            name='CreatedAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 14, 19, 34, 444290)),
        ),
        migrations.AlterField(
            model_name='comic',
            name='UpdateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 14, 19, 34, 444290)),
        ),
        migrations.AlterField(
            model_name='comiccomment',
            name='CreateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 14, 19, 34, 449956)),
        ),
    ]
