from django.db import models

# Create your models here.


class StatusCrm(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=200, verbose_name='Название статуса')
    
    def __str__(self):
        return self.status_name
    
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Order(models.Model):
    order_id = models.AutoField(primary_key=True, verbose_name='Идентификатор заказа')
    order_dt = models.DateTimeField(auto_now=True, verbose_name='Дата')
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return f'Заказ {self.order_id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class CommentCrm(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Заявка')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата написания')
    comment_text = models.TextField(verbose_name='Текст комментария')
    
    def __str__(self):
        return self.comment_text
    
    class Meta:
        verbose_name = 'Комментарий к заявке'
        verbose_name_plural = 'Комментарии'