# Generated by Django 3.2.6 on 2021-09-09 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_auto_20210910_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
