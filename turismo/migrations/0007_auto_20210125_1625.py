# Generated by Django 3.1.5 on 2021-01-25 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turismo', '0006_contacto'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Regione',
            new_name='Regiones',
        ),
        migrations.AlterField(
            model_name='turista',
            name='Run',
            field=models.CharField(max_length=10),
        ),
    ]
