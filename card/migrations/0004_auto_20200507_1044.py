# Generated by Django 2.0.5 on 2020-05-07 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_simulation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='simulation',
            options={'ordering': ['-consume_time'], 'verbose_name': '消费表', 'verbose_name_plural': '消费表'},
        ),
        migrations.AlterModelTable(
            name='simulation',
            table='simulation',
        ),
    ]
