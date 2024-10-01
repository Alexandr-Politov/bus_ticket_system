# Generated by Django 5.1.1 on 2024-09-30 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0003_bus_facilities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='station.order'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='station.trip'),
        ),
    ]