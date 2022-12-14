# Generated by Django 4.1 on 2022-09-01 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='admin')),
                ('descripcion', models.CharField(max_length=300)),
                ('precio', models.FloatField()),
                ('unidades', models.IntegerField()),
            ],
        ),
    ]
