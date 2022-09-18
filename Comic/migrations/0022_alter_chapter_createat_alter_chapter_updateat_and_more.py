# Generated by Django 4.1 on 2022-09-17 11:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0008_remove_account_profile_profile_account'),
        ('Comic', '0021_comment_alter_chapter_createat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='CreateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 18, 23, 38, 33556)),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='UpdateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 18, 23, 38, 33556)),
        ),
        migrations.AlterField(
            model_name='comic',
            name='CreatedAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 18, 23, 38, 30563)),
        ),
        migrations.AlterField(
            model_name='comic',
            name='UpdateAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 18, 23, 38, 30563)),
        ),
        migrations.CreateModel(
            name='CommentComic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=datetime.datetime(2022, 9, 17, 18, 23, 38, 34552))),
                ('Content', models.TextField()),
                ('Chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Comic.chapter')),
                ('Comic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Comic.comic')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.profile')),
            ],
        ),
        migrations.AlterField(
            model_name='repcomment',
            name='Comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='Comic.commentcomic'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
