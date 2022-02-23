# Generated by Django 4.0 on 2022-02-21 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposedPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposed_price', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.user')),
            ],
        ),
    ]