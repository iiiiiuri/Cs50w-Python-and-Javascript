# Generated by Django 4.2.5 on 2023-12-07 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_alter_auctionlisting_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='last_bid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_bid', to='auctions.bid'),
        ),
    ]