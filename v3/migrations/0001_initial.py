# Generated by Django 5.0.2 on 2024-03-18 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(max_length=200, upload_to='v3/skins/')),
                ('model', models.CharField(default='geometry.humanoid.customSlim', max_length=30)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SkinList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='skinpack', max_length=30)),
                ('skin', models.ManyToManyField(blank=True, related_name='cont', to='v3.skin')),
            ],
        ),
    ]
