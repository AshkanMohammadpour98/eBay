# Generated by Django 4.0 on 2022-02-21 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_list_slug_list_status_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='category',
            field=models.ManyToManyField(related_name='list_category', to='lists.Category'),
        ),
    ]
