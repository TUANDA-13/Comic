# Generated by Django 4.1 on 2022-09-17 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comic', '0027_commentcomic_alter_chapter_createat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='repcomment',
            name='CreateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 19, 54, 29, 859424)),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='CreateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 19, 54, 29, 857341)),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='UpdateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 19, 54, 29, 857341)),
        ),
        migrations.AlterField(
            model_name='comic',
            name='CreatedAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 19, 54, 29, 853373)),
        ),
        migrations.AlterField(
            model_name='comic',
            name='UpdateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 19, 54, 29, 853373)),
        ),
        migrations.AlterField(
            model_name='commentcomic',
            name='CreateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 19, 54, 29, 858338)),
        ),
    ]
