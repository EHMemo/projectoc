# Generated by Django 5.0.6 on 2024-06-28 07:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NyaaaStore', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Carrito',
            new_name='Cart',
        ),
        migrations.RenameModel(
            old_name='CarritoItem',
            new_name='CartItem',
        ),
        migrations.AlterField(
            model_name='producto',
            name='tp_producto',
            field=models.CharField(choices=[('F', 'FIGURA'), ('A', 'ACCESORIO'), ('N', 'SIN ESPECIFICAR'), ('P', 'POLERA')], default='SIN ESPECIFICAR', max_length=1),
        ),
        migrations.AlterField(
            model_name='userperfil',
            name='city',
            field=models.CharField(choices=[('Santiago', 'Santiago'), ('Tome', 'Tome'), ('San Pedro', 'San Pedro'), ('Valparaíso', 'Valparaíso'), ('Concepción', 'Concepción')], max_length=15),
        ),
        migrations.AlterField(
            model_name='venta',
            name='estado',
            field=models.CharField(choices=[('PREPARADO', 'PREPARADO'), ('ENVIADO', 'ENVIADO'), ('EN PREPARACIÓN', 'EN PREPARACIÓN'), ('ENTREGADO', 'ENTREGADO')], default='EN PREPARACIÓN', max_length=30),
        ),
    ]
