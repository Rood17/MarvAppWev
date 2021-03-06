# Generated by Django 4.0.1 on 2022-02-19 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_imagenes_subheader_destacada1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='portafolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('E', 'Equipo'), ('v', 'Evento')], default='E', max_length=1, verbose_name='Tipo')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('descripcion', models.TextField(max_length=200, verbose_name='Breve descripción')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('clase', models.ForeignKey(default='', help_text='Seleccione la clase de servicios.', on_delete=django.db.models.deletion.CASCADE, to='core.servicios', verbose_name='Servicio')),
            ],
            options={
                'verbose_name': 'Portafolio',
                'verbose_name_plural': 'Portafolio',
                'ordering': ['-created'],
            },
        ),
    ]
