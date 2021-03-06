# Generated by Django 4.0.1 on 2022-02-21 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_contacto_alter_faqs_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacto',
            options={'ordering': ['name'], 'verbose_name': 'enlace', 'verbose_name_plural': 'enlaces'},
        ),
        migrations.RemoveField(
            model_name='contacto',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='contacto',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='contacto',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='contacto',
            name='key',
            field=models.SlugField(default='', max_length=100, unique=True, verbose_name='Nombre clave'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacto',
            name='name',
            field=models.CharField(default='', max_length=200, verbose_name='Red social o Número'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacto',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Enlace'),
        ),
        migrations.AlterField(
            model_name='categorias',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='categorias',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
        migrations.AlterField(
            model_name='faqs',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='faqs',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
        migrations.AlterField(
            model_name='imagenes',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='imagenes',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
        migrations.AlterField(
            model_name='paquetes',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='paquetes',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
    ]
