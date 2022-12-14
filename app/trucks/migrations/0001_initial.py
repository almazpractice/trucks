# Generated by Django 2.2.19 on 2022-11-29 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TruckType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('load_capacity', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Тип самосвала',
                'verbose_name_plural': 'Типы самосвала',
            },
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_number', models.CharField(db_index=True, max_length=20)),
                ('cur_capacity', models.PositiveIntegerField()),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='truck', to='trucks.TruckType')),
            ],
            options={
                'verbose_name': 'Самосвал',
                'verbose_name_plural': 'Самосвалы',
            },
        ),
    ]
