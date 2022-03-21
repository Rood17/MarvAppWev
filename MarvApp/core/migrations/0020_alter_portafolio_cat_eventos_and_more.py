# Generated by Django 4.0.1 on 2022-03-10 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_cateventos_portafolio_cat_eventos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portafolio',
            name='cat_eventos',
            field=models.ManyToManyField(help_text='Seleccione una o varios eventos relacionadas al item.', null=True, to='core.CatEventos', verbose_name='Eventos'),
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='categoria',
            field=models.ManyToManyField(help_text='Seleccione una o varias categorías relacionadas al item.', null=True, to='core.Categorias', verbose_name='Categorías'),
        ),
    ]
