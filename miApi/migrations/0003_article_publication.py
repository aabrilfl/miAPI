# Generated by Django 3.2 on 2021-04-22 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApi', '0002_auto_20210420_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
                ('publications_list', models.ManyToManyField(to='miApi.Publication')),
            ],
        ),
    ]
