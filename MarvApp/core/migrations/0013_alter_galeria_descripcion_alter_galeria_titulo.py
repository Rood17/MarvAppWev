# Generated by Django 4.0.1 on 2022-02-19 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_galeria_alter_imagenes_destacada2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria',
            name='descripcion',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Breve descripción'),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='titulo',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Título'),
        ),
    ]
