# Generated by Django 4.1.2 on 2023-04-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vente', '0006_alter_restaurateur_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurateur',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]