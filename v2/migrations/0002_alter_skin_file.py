# Generated by Django 4.2.7 on 2024-01-04 01:14

from django.db import migrations, models
import v2.models


class Migration(migrations.Migration):

    dependencies = [
        ('v2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skin',
            name='file',
            field=models.ImageField(upload_to=v2.models.UploadPath),
        ),
    ]