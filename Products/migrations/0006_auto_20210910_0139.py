# Generated by Django 3.2.6 on 2021-09-09 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_auto_20210909_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
