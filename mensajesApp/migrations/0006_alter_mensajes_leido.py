# Generated by Django 4.1.4 on 2023-01-21 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensajesApp', '0005_alter_mensajes_emisor_alter_mensajes_receptor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='leido',
            field=models.BooleanField(default=False, null=True),
        ),
    ]