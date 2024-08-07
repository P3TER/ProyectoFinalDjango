# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'
        app_label = "appngvdj"


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)
        app_label = "appngvdj"


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)
        app_label = "appngvdj"


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
        app_label = "appngvdj"


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)
        app_label = "appngvdj"


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)
        app_label = "appngvdj"


class Autores(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'autores'
        app_label = "appngvdj"


class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=75)

    class Meta:
        managed = False
        db_table = 'categorias'
        app_label = "appngvdj"


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    identificacion = models.CharField(max_length=12)
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    direccion = models.CharField(max_length=128, blank=True, null=True)
    telefono = models.CharField(max_length=14)
    correo = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'clientes'
        app_label = "appngvdj"


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        app_label = "appngvdj"
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)
        app_label = "appngvdj"


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
        app_label = "appngvdj"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
        app_label = "appngvdj"


class LibroXAutor(models.Model):
    isbn = models.OneToOneField('Libros', models.DO_NOTHING, db_column='isbn', primary_key=True)  # The composite primary key (isbn, id_autor) found, that is not supported. The first column is selected.
    id_autor = models.ForeignKey(Autores, models.DO_NOTHING, db_column='id_autor')

    class Meta:
        managed = False
        db_table = 'libro_x_autor'
        unique_together = (('isbn', 'id_autor'),)
        app_label = "appngvdj"


class Libros(models.Model):
    isbn = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=128)
    fecha_pub = models.DateField()
    precio = models.FloatField()
    id_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='id_categoria')
    cantidad_stock = models.IntegerField()
    portada = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'libros'
        app_label = "appngvdj"


class PedidoXCliente(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente')
    isbn = models.ForeignKey(Libros, models.DO_NOTHING, db_column='isbn')
    cantidad = models.IntegerField()
    fecha_ped = models.DateField()

    class Meta:
        managed = False
        app_label = "appngvdj"
        db_table = 'pedido_x_cliente'
