# Generated by Django 4.2.4 on 2023-09-01 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escola',
            name='nome',
            field=models.CharField(choices=[('DADOS', 'Data'), ('TECNOLOGIA', 'Technology'), ('PRODUTO', 'Product')], max_length=20, unique=True),
        ),
    ]
