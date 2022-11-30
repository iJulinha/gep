# Generated by Django 2.2.19 on 2022-11-30 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='contato',
            field=models.CharField(max_length=14, null=True, verbose_name='Número de contato'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='cpf',
            field=models.CharField(max_length=14, null=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='bairro',
            field=models.CharField(max_length=100, null=True, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cep',
            field=models.CharField(help_text='Format: XXXXX-XXX', max_length=9, null=True, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='complemento',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='logradouro',
            field=models.CharField(max_length=100, null=True, verbose_name='Logradouro'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='nome',
            field=models.CharField(max_length=100, null=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='numero',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número'),
        ),
    ]