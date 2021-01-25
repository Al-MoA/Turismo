# Generated by Django 3.1.5 on 2021-01-25 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turismo', '0004_auto_20210124_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Run', models.TextField()),
                ('Nombre', models.CharField(max_length=100)),
                ('Telefono', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
