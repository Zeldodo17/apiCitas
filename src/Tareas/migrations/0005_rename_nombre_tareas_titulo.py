# Generated by Django 4.0.1 on 2022-02-09 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tareas', '0004_alter_tareas_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tareas',
            old_name='nombre',
            new_name='titulo',
        ),
    ]
