# Generated by Django 4.1 on 2022-09-07 08:34

import Comic.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comic', '0005_alter_chapter_createat_alter_chapter_updateat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='CreateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 7, 15, 34, 39, 326159)),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='NumberChapter',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='UpdateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 7, 15, 34, 39, 326159)),
        ),
        migrations.AlterField(
            model_name='comic',
            name='Banner',
            field=models.ImageField(null=True, upload_to=Comic.models.Comic.update_filename),
        ),
        migrations.AlterField(
            model_name='comic',
            name='CreatedAt',
            field=models.DateField(default=datetime.datetime(2022, 9, 7, 15, 34, 39, 321171)),
        ),
        migrations.AlterField(
            model_name='comic',
            name='Status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Updating', 'Updating'), ('Draft', 'Draft')], default=('Completed', 'Completed'), max_length=20),
        ),
        migrations.AlterField(
            model_name='comic',
            name='UpdateAt',
            field=models.DateField(default=datetime.datetime(2022, 9, 7, 15, 34, 39, 321171)),
        ),
    ]
