# Generated by Django 4.0 on 2022-02-21 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
        ('lists', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='list',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='lists.list'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auctions.user'),
        ),
    ]
