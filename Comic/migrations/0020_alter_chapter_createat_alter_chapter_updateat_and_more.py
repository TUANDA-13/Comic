# Generated by Django 4.1 on 2022-09-15 07:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comic', '0019_alter_chapter_createat_alter_chapter_updateat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='CreateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 15, 14, 3, 56, 601120)),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='UpdateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 15, 14, 3, 56, 601120)),
        ),
        migrations.AlterField(
            model_name='comic',
            name='CreatedAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 15, 14, 3, 56, 596507)),
        ),
        migrations.AlterField(
            model_name='comic',
            name='UpdateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 15, 14, 3, 56, 596507)),
        ),
    ]
