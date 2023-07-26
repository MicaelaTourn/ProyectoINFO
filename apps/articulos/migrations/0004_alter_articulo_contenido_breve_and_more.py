# Generated by Django 4.2.3 on 2023-07-26 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articulos', '0003_alter_articulo_categoria_articulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='contenido_breve',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='usuario_articulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
