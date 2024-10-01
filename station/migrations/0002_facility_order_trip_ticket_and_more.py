# Generated by Django 5.1.1 on 2024-09-28 14:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'facilities',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=63)),
                ('destination', models.CharField(max_length=63)),
                ('departure', models.DateTimeField()),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station.bus')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station.order')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station.trip')),
            ],
        ),
        migrations.AddIndex(
            model_name='trip',
            index=models.Index(fields=['source', 'destination'], name='station_tri_source_1ae98f_idx'),
        ),
        migrations.AddIndex(
            model_name='trip',
            index=models.Index(fields=['departure'], name='station_tri_departu_683ffd_idx'),
        ),
        migrations.AddConstraint(
            model_name='ticket',
            constraint=models.UniqueConstraint(fields=('seat', 'trip'), name='unique_ticket_seat_trip'),
        ),
    ]
