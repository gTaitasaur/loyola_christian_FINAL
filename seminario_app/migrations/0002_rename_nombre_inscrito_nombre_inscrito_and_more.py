# Generated by Django 4.2.7 on 2023-12-22 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminario_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscrito',
            old_name='nombre',
            new_name='nombre_inscrito',
        ),
        migrations.RenameField(
            model_name='institucion',
            old_name='nombre',
            new_name='nombre_institucion',
        ),
    ]