# Generated by Django 3.2.2 on 2021-05-26 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licence_place', models.CharField(max_length=255)),
                ('vehicle_type', models.CharField(choices=[('car', 'car'), ('motorcycle', 'motorcycle')], max_length=255)),
                ('arrived_at', models.DateTimeField(auto_now_add=True)),
                ('paid_at', models.DateTimeField(null=True)),
                ('amount_paid', models.IntegerField(null=True)),
                ('space', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='parking.spacemodel')),
            ],
        ),
    ]
