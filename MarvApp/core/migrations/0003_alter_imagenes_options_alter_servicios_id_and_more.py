# Generated by Django 4.0.1 on 2022-01-27 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_imagenes_remove_servicios_headimg1_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagenes',
            options={'ordering': ['-created'], 'verbose_name': 'Imágenes', 'verbose_name_plural': 'Imágenes'},
        ),
        migrations.AlterField(
            model_name='servicios',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='subHeader',
            field=models.TextField(max_length=200, verbose_name='Texto descriptivo Header'),
        ),
    ]
