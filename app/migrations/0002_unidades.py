# Generated by Django 4.0.1 on 2022-01-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nindentifica', models.CharField(max_length=50)),
                ('proprietario', models.CharField(max_length=30)),
                ('condominio', models.CharField(max_length=30)),
                ('endereco', models.CharField(max_length=30)),
            ],
        ),
    ]
