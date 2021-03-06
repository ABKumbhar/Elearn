# Generated by Django 3.0.5 on 2020-05-19 08:45

import Main.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0011_auto_20200515_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='PreviewFile',
        ),
        migrations.RemoveField(
            model_name='module',
            name='File',
        ),
        migrations.CreateModel(
            name='ModuleFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File', models.FileField(blank=True, null=True, upload_to=Main.models.upload_path)),
                ('modulefile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moudulefile', to='Main.Module')),
            ],
        ),
        migrations.CreateModel(
            name='CourseFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PreviewFile', models.FileField(blank=True, null=True, upload_to=Main.models.upload_path)),
                ('coursefile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coursefile', to='Main.Course')),
            ],
        ),
    ]
