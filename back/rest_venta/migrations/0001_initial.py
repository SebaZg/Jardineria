# Generated by Django 4.0.5 on 2022-07-14 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rest_auth', '0001_initial'),
        ('rest_producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoVenta',
            fields=[
                ('idEstadoVenta', models.AutoField(primary_key=True, serialize=False, verbose_name='id estado Venta')),
                ('nombreEstadoVenta', models.CharField(max_length=255, verbose_name='nombre estado venta')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idVenta', models.AutoField(primary_key=True, serialize=False, verbose_name='id de venta')),
                ('fechaVenta', models.DateField(auto_now_add=True, null=True, verbose_name='fecha de venta')),
                ('totalVenta', models.IntegerField(verbose_name='total de venta')),
                ('estadoVenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_venta.estadoventa', verbose_name='EstadoVenta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_auth.usuario', verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('idDetalleVenta', models.AutoField(primary_key=True, serialize=False, verbose_name='id Detalle Venta')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_producto.producto', verbose_name='producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_venta.venta', verbose_name='venta')),
            ],
        ),
    ]