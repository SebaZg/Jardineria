# Generated by Django 4.0.5 on 2022-07-14 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False, verbose_name='id categoria')),
                ('nombreCategoria', models.CharField(max_length=255, verbose_name='nombre categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='id de producto')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre de producto')),
                ('valor', models.IntegerField(verbose_name='Valor de producto')),
                ('descripcion', models.CharField(max_length=1500, verbose_name='Descripcion de producto')),
                ('stock', models.IntegerField(default=0, verbose_name='Stock de producto')),
                ('imagen', models.CharField(max_length=512, verbose_name='Imagen de producto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_producto.categoria', verbose_name='Categoria de producto')),
            ],
        ),
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('idPromocion', models.AutoField(primary_key=True, serialize=False, verbose_name='id promocion')),
                ('pordesct', models.IntegerField(verbose_name='porcentaje de descuento')),
                ('descripcion', models.CharField(max_length=512, null=True, verbose_name='descripcion de promoción')),
            ],
        ),
        migrations.CreateModel(
            name='PromocionProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_producto.producto')),
                ('idPromocion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_producto.promocion')),
            ],
        ),
    ]
