# Generated by Django 4.0.3 on 2022-03-25 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carinstance',
            name='inv_num',
        ),
        migrations.AddField(
            model_name='car',
            name='num',
            field=models.CharField(help_text='Введите номер автомобиля в автопарке', max_length=20, null=True, verbose_name='Номер автомобиля в парке'),
        ),
    ]
