# Generated by Django 4.2.3 on 2023-07-28 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0004_alter_articulo_contenido_breve_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='contenido_breve',
            field=models.TextField(),
        ),
    ]
