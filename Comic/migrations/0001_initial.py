# Generated by Django 4.1 on 2022-09-04 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Special', models.BooleanField(default=False)),
                ('Decreption', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author', models.CharField(max_length=40)),
                ('Status', models.CharField(choices=[('Boy', 'Boy'), ('Girl', 'Girl'), ('Other', 'Other')], default=('Boy', 'Boy'), max_length=20)),
                ('Views', models.BigIntegerField(default=0)),
                ('Context', models.TextField()),
                ('Slug', models.SlugField()),
                ('Categories', models.ManyToManyField(to='Comic.category')),
            ],
        ),
    ]
