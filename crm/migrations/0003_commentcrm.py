# Generated by Django 3.2.7 on 2021-09-06 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20210906_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentCrm',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_dt', models.DateTimeField(auto_now=True, verbose_name='Дата написания')),
                ('comment_text', models.TextField(verbose_name='Текст комментария')),
                ('comment_binding', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.order', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'Комментарий к заявке',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
