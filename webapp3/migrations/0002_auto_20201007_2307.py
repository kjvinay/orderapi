# Generated by Django 3.1.1 on 2020-10-08 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='purchased_ON',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='productname',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
