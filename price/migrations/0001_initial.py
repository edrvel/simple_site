# Generated by Django 3.2.7 on 2021-09-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceCard',
            fields=[
                ('pc_id', models.AutoField(primary_key=True, serialize=False)),
                ('pc_value', models.CharField(max_length=200, verbose_name='Цена')),
                ('pc_description', models.CharField(max_length=200, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('pt_id', models.AutoField(primary_key=True, serialize=False)),
                ('pt_title', models.CharField(max_length=200, verbose_name='Название')),
                ('pt_old_price', models.CharField(max_length=200, verbose_name='Старая цена')),
                ('pt_new_price', models.CharField(max_length=200, verbose_name='Новая цена')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
