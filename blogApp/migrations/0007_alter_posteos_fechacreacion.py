# Generated by Django 4.1.4 on 2023-01-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0006_alter_posteos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteos',
            name='fechaCreacion',
            field=models.DateField(null=True),
        ),
    ]