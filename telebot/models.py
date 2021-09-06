from django.db import models

# Create your models here.


class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен бота Telegram')
    tg_chat = models.CharField(max_length=200, verbose_name='id чата с ботом')
    tg_message = models.TextField(verbose_name='Текст сообщения для чата')
    
    def __str__(self):
        return self.tg_chat
    
    class Meta:
        verbose_name = 'Настройка бота Telegram'
        verbose_name_plural = 'Настройки бота Telegram'