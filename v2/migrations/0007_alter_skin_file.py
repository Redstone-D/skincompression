# Generated by Django 5.0.2 on 2024-03-18 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v2', '0006_alter_skin_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skin',
            name='file',
            field=models.ImageField(max_length=200, upload_to='v2/skins/'),
        ),
    ]
