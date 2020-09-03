# Generated by Django 3.1 on 2020-08-21 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0003_auto_20200821_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='item',
            new_name='item_name',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
