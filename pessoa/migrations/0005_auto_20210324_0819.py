# Generated by Django 3.1.1 on 2021-03-24 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0004_auto_20210324_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='dados',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pessoa.pessoa', verbose_name='Dados Funcionario'),
        ),
    ]