# Generated by Django 3.2.7 on 2021-09-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeleSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_token', models.CharField(max_length=200, verbose_name='Токен бота Telegram')),
                ('tg_chat', models.CharField(max_length=200, verbose_name='id чата с ботом')),
                ('tg_message', models.TextField(verbose_name='Текст сообщения для чата')),
            ],
            options={
                'verbose_name': 'Настройка бота Telegram',
                'verbose_name_plural': 'Настройки бота Telegram',
            },
        ),
    ]
