# Generated by Django 3.0.5 on 2020-05-11 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_module_index_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='index_number',
            field=models.IntegerField(null=True),
        ),
    ]
