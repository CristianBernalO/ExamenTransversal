# Generated by Django 4.1.2 on 2024-07-10 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('idAutor', models.AutoField(db_column='id_autor', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(db_column='id_categoria', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('idLibro', models.AutoField(db_column='id_libro', primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('anioPublicacion', models.CharField(max_length=4)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NavItem',
            fields=[
                ('idNavItem', models.AutoField(db_column='id_nav_item', primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=150)),
            ],
        ),
    ]
