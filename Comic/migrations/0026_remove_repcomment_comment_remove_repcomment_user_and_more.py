# Generated by Django 4.1 on 2022-09-17 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comic', '0025_alter_chapter_createat_alter_chapter_updateat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repcomment',
            name='Comment',
        ),
        migrations.RemoveField(
            model_name='repcomment',
            name='User',
        ),
        migrations.AlterField(
            model_name='chapter',
            name='CreateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 18, 36, 48, 402688)),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='UpdateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 18, 36, 48, 402688)),
        ),
        migrations.AlterField(
            model_name='comic',
            name='CreatedAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 18, 36, 48, 398648)),
        ),
        migrations.AlterField(
            model_name='comic',
            name='UpdateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 18, 36, 48, 398648)),
        ),
        migrations.DeleteModel(
            name='CommentComic',
        ),
        migrations.DeleteModel(
            name='RepComment',
        ),
    ]
