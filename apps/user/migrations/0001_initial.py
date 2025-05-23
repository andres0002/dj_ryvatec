# Generated by Django 5.2 on 2025-05-15 15:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.CharField(max_length=10, primary_key=10, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_user', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=60)),
                ('correo', models.EmailField(blank=True, max_length=150, null=True)),
                ('pagina', models.CharField(max_length=150)),
                ('imagen', models.ImageField(default='usuarios/ironman.jpg', upload_to='usuarios')),
                ('especialidad', models.CharField(max_length=100)),
                ('rol', models.CharField(choices=[('AMD', 'Administrador'), ('PRO', 'Proveedor'), ('TEC', 'Tecnico')], max_length=20)),
                ('usuid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id_dispositivo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='dispositivos')),
                ('descripcion', models.CharField(max_length=250)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usuario')),
            ],
            options={
                'verbose_name': 'Dispositivo',
                'verbose_name_plural': 'Dispositivos',
            },
        ),
    ]
