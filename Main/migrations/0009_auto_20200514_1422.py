# Generated by Django 3.0.5 on 2020-05-14 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0008_auto_20200514_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='skype_name',
            new_name='skype_ID',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='skype_name',
            new_name='skype_ID',
        ),
    ]
