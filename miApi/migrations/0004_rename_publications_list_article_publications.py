# Generated by Django 3.2 on 2021-04-22 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miApi', '0003_article_publication'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='publications_list',
            new_name='publications',
        ),
    ]
