# Generated by Django 4.0 on 2022-11-14 18:25

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
                ('id_categoria', models.AutoField(db_column='ID_Categoria', primary_key=True, serialize=False)),
                ('descripcion_categoria', models.CharField(blank=True, db_column='Descripcion_Categoria', max_length=100, null=True)),
                ('estado_categoria', models.BooleanField(db_column='Estado_Categoria')),
                ('fecharegistrocategoria', models.DateField(db_column='FechaRegistroCategoria')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(db_column='ID_Cliente', primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(db_column='Nombre_Cliente', max_length=50)),
                ('apellido_cliente', models.CharField(db_column='Apellido_Cliente', max_length=50)),
                ('correo_cliente', models.CharField(db_column='Correo_Cliente', max_length=50)),
                ('clave_cliente', models.CharField(db_column='Clave_Cliente', max_length=50)),
                ('telefono_cliente', models.CharField(db_column='Telefono_Cliente', max_length=50)),
                ('fecharegistrocliente', models.DateField(db_column='FechaRegistroCliente')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id_compra', models.AutoField(db_column='ID_Compra', primary_key=True, serialize=False)),
                ('tipodocumento_compra', models.CharField(db_column='TipoDocumento_Compra', max_length=50)),
                ('numerodocumento_compra', models.CharField(db_column='NumeroDocumento_Compra', max_length=50)),
                ('montototal_compra', models.IntegerField(db_column='MontoTotal_Compra')),
                ('fecharegistrocompra', models.DateField(db_column='FechaRegistroCompra')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(db_column='ID_Proveedor', primary_key=True, serialize=False)),
                ('rutempresa', models.CharField(db_column='RutEmpresa', max_length=50)),
                ('dvempresa', models.CharField(db_column='DVEmpresa', max_length=1)),
                ('razonsocial', models.CharField(db_column='RazonSocial', max_length=50)),
                ('correo', models.CharField(db_column='Correo', max_length=50)),
                ('telefono', models.CharField(db_column='Telefono', max_length=50)),
                ('fecharegistroproveedor', models.DateField(db_column='FechaRegistroProveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(db_column='ID_Rol', primary_key=True, serialize=False)),
                ('descripcion_rol', models.CharField(db_column='Descripcion_Rol', max_length=50)),
                ('fecharegistrorol', models.DateField(db_column='FechaRegistroRol')),
                ('id_permiso', models.IntegerField(db_column='ID_Permiso')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(db_column='ID_Usuario', primary_key=True, serialize=False)),
                ('rut_usuario', models.CharField(db_column='Rut_Usuario', max_length=50)),
                ('dv_usuario', models.CharField(db_column='DV_Usuario', max_length=1)),
                ('nombre_usuario', models.CharField(db_column='Nombre_Usuario', max_length=50)),
                ('apellidos_usuario', models.CharField(db_column='Apellidos_Usuario', max_length=50)),
                ('correo_usuario', models.CharField(db_column='Correo_Usuario', max_length=50)),
                ('clave_usuario', models.CharField(db_column='Clave_Usuario', max_length=50)),
                ('telefono_usuario', models.CharField(db_column='Telefono_Usuario', max_length=50)),
                ('estado_usuario', models.BooleanField(db_column='Estado_Usuario')),
                ('fecharegistrousuario', models.DateField(db_column='FechaRegistroUsuario')),
                ('rol_id_rol', models.ForeignKey(db_column='ROL_ID_Rol', on_delete=django.db.models.deletion.DO_NOTHING, to='TragonBall.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(db_column='ID_Venta', primary_key=True, serialize=False)),
                ('tipodocumento_venta', models.CharField(db_column='TipoDocumento_Venta', max_length=50)),
                ('numerodocumento_venta', models.CharField(db_column='NumeroDocumento_Venta', max_length=50)),
                ('nombrecliente', models.CharField(db_column='NombreCliente', max_length=50)),
                ('montopago_venta', models.DecimalField(db_column='MontoPago_Venta', decimal_places=0, max_digits=28)),
                ('montovuelto_venta', models.DecimalField(db_column='MontoVuelto_Venta', decimal_places=0, max_digits=28)),
                ('montototal_venta', models.DecimalField(db_column='MontoTotal_Venta', decimal_places=0, max_digits=28)),
                ('fecharegistroventa', models.DateField(db_column='FechaRegistroVenta')),
                ('cliente_id_cliente', models.ForeignKey(db_column='CLIENTE_ID_Cliente', on_delete=django.db.models.deletion.DO_NOTHING, to='TragonBall.cliente')),
                ('usuario_id_usuario', models.ForeignKey(db_column='USUARIO_ID_Usuario', on_delete=django.db.models.deletion.DO_NOTHING, to='TragonBall.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id_pago', models.AutoField(db_column='ID_Pago', primary_key=True, serialize=False)),
                ('metodopago', models.CharField(db_column='MetodoPago', max_length=50)),
                ('montopago', models.CharField(db_column='MontoPago', max_length=50)),
                ('fecharegistrotipopago', models.DateField(db_column='FechaRegistroTipoPago')),
                ('venta_id_venta', models.ForeignKey(db_column='VENTA_ID_Venta', on_delete=django.db.models.deletion.DO_NOTHING, to='TragonBall.venta')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoElaborado',
            fields=[
                ('id_producto', models.AutoField(db_column='ID_Producto', primary_key=True, serialize=False)),
                ('codigo_producto', models.CharField(blank=True, db_column='Codigo_Producto', max_length=50, null=True)),
                ('nombre_producto', models.CharField(db_column='Nombre_Producto', max_length=50)),
                ('descripcion_producto', models.CharField(blank=True, db_column='Descripcion_Producto', max_length=200, null=True)),
                ('stock_producto', models.IntegerField(db_column='Stock_Producto')),
                ('preciocompra', models.CharField(db_column='PrecioCompra', max_length=50)),
                ('precioventa', models.DecimalField(db_column='PrecioVenta', decimal_places=2, max_digits=5)),
                ('estado_producto', models.BooleanField(db_column='Estado_Producto')),
                ('fecharegistroproducto', models.DateField(db_column='FechaRegistroProducto')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='Imagen')),
                ('categoria_id_categoria', models.ForeignKey(db_column='CATEGORIA_ID_Categoria', on_delete=django.db.models.deletion.DO_NOTHING, to='TragonBall.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id_permiso', models.AutoField(db_column='ID_Permiso', primary_key=True, serialize=False)),
                ('nombremenu', models.CharField(db_column='NombreMenu', max_length=100)),
                ('fecharegistropermiso', models.DateField(db_column='FechaRegistroPermiso')),
                ('id_rol', models.ForeignKey(db_column='ID_Rol', on_delete=django.db.models.deletion.DO_NOTHING, to='TragonBall.rol')),
            ],
        ),
        migrations.CreateModel(
            name='MateriaPrima',
            fields=[
                ('id_materiaprima', models.AutoField(db_column='ID_MateriaPrima', primary_key=True, serialize=False)),
                ('codigo_materiaprima', models.CharField(blank=True, db_column='Codigo_MateriaPrima', max_length=50, null=True)),
                ('nombre_materiaprima', models.CharField(db_column='Nombre_MateriaPrima', max_length=50)),
                ('descripcion_materiaprima', models.CharField(blank=True, db_column='Descripcion_MateriaPrima', max_length=100, null=True)),
                ('stock_materiaprima', models.DecimalField(db_column='Stock_MateriaPrima', decimal_places=0, max_digits=28)),
                ('preciocompra_materiaprima', models.DecimalField(db_column='PrecioCompra_MateriaPrima', decimal_places=0, max_digits=28)),
                ('estado_materiaprima', models.BooleanField(db_column='Estado_MateriaPrima')),
                ('fecharegistro_materiaprima', models.DateField(db_column='FechaRegistro_MateriaPrima')),
                ('categoria_id_categoria', models.ForeignKey(db_column='CATEGORIA_ID_Categoria', on_delete=django.db.models.deletion.DO_NOTHING, to='TragonBall.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id_detalleventa', models.AutoField(db_column='ID_DetalleVenta', primary_key=True, serialize=False)),
                ('precioventa', models.IntegerField(db_column='PrecioVenta')),
                ('cantidad_detalleventa', models.IntegerField(db_column='Cantidad_DetalleVenta')),
                ('subtotal_detalleventa', models.IntegerField(db_column='SubTotal_DetalleVenta')),
                ('fecharegistrodetalleventa', models.DateField(db_column='FechaRegistroDetalleVenta')),
                ('producto_elaborado_id_producto', models.ForeignKey(db_column='PRODUCTO_ELABORADO_ID_Producto', on_delete=django.db.models.deletion.DO_NOTHING, to='TragonBall.productoelaborado')),
                ('venta_id_venta', models.ForeignKey(db_column='VENTA_ID_Venta', on_delete=django.db.models.deletion.DO_NOTHING, to='TragonBall.venta')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id_detallecompra', models.AutoField(db_column='ID_DetalleCompra', primary_key=True, serialize=False)),
                ('preciocompra', models.IntegerField(db_column='PrecioCompra')),
                ('precioventa', models.IntegerField(db_column='PrecioVenta')),
                ('cantidad_detallecompra', models.IntegerField(db_column='Cantidad_DetalleCompra')),
                ('montototal_detallecompra', models.IntegerField(db_column='MontoTotal_DetalleCompra')),
                ('fecharegistrodetallecompra', models.DateField(db_column='FechaRegistroDetalleCompra')),
                ('compra_id_compra', models.ForeignKey(db_column='COMPRA_ID_Compra', on_delete=django.db.models.deletion.DO_NOTHING, to='TragonBall.compra')),
                ('materia_prima_id_materiaprima', models.ForeignKey(db_column='MATERIA_PRIMA_ID_MateriaPrima', on_delete=django.db.models.deletion.DO_NOTHING, to='TragonBall.materiaprima')),
            ],
        ),
        migrations.CreateModel(
            name='CompraPaypal',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=100)),
                ('codigo_estado', models.CharField(max_length=100)),
                ('total_de_la_compra', models.CharField(max_length=50)),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('apellido_cliente', models.CharField(max_length=100)),
                ('correo_cliente', models.CharField(max_length=100)),
                ('direccion_cliente', models.CharField(max_length=100)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='TragonBall.productoelaborado')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='proveedor_id_proveedor',
            field=models.ForeignKey(db_column='PROVEEDOR_ID_Proveedor', on_delete=django.db.models.deletion.DO_NOTHING, to='TragonBall.proveedor'),
        ),
        migrations.AddField(
            model_name='compra',
            name='usuario_id_usuario',
            field=models.ForeignKey(db_column='USUARIO_ID_Usuario', on_delete=django.db.models.deletion.DO_NOTHING, to='TragonBall.usuario'),
        ),
    ]
