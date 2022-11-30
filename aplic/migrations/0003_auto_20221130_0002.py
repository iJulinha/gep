# Generated by Django 2.2.19 on 2022-11-30 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0002_auto_20221129_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='contato',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='Número de contato'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='data_nascimento',
            field=models.DateField(help_text='Por favor use o seguinte formato: <em>DD/MM/YYYY', null=True, verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='numero',
            field=models.IntegerField(null=True, verbose_name='Número'),
        ),
    ]