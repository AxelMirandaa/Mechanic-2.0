# Generated by Django 3.2.3 on 2021-06-14 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210613_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='id',
        ),
        migrations.AlterField(
            model_name='servicio',
            name='nombre_servicio',
            field=models.CharField(max_length=25, primary_key=True, serialize=False, verbose_name='Nombre Servicio'),
        ),
    ]
