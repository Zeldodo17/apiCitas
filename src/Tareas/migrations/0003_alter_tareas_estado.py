# Generated by Django 4.0.1 on 2022-02-07 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tareas', '0002_alter_tareas_options_alter_tareas_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='estado',
            field=models.CharField(default='Incompleto', max_length=150),
        ),
    ]