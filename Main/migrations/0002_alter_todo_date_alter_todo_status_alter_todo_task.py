# Generated by Django 4.0.1 on 2022-02-22 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateField(verbose_name='Sana'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Holati'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='task',
            field=models.CharField(max_length=255, verbose_name="Ma'lumot"),
        ),
    ]
