# Generated by Django 3.0.5 on 2020-05-13 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_auto_20200513_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Linkdein',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]