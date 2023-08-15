# Generated by Django 4.2.4 on 2023-08-11 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('idProdut', models.AutoField(primary_key=True, serialize=False)),
                ('eanProdut', models.CharField(max_length=100, verbose_name='Ean')),
                ('nomProdut', models.CharField(max_length=100, verbose_name='Nome')),
                ('desProdut', models.CharField(max_length=100, verbose_name='Descricao')),
                ('preProdut', models.FloatField()),
                ('imgProdut', models.ImageField(null=True, upload_to='images/', verbose_name='Imagem')),
            ],
        ),
    ]
