# Generated by Django 4.0.1 on 2022-02-19 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_galeria_descripcion_alter_galeria_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeria',
            name='clase',
            field=models.ManyToManyField(help_text='Seleccione una o las dos clases de servicio.', to='core.Servicios', verbose_name='Servicio relacionado'),
        ),
    ]
