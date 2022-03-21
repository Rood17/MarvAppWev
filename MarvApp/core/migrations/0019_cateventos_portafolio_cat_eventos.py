# Generated by Django 4.0.1 on 2022-03-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_contacto_options_remove_contacto_facebook_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatEventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Título')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Tipo de Eventos',
                'verbose_name_plural': 'Tipo de Eventos',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='portafolio',
            name='cat_eventos',
            field=models.ManyToManyField(help_text='Seleccione una o varios eventos relacionadas al item.', to='core.CatEventos', verbose_name='Eventos'),
        ),
    ]
