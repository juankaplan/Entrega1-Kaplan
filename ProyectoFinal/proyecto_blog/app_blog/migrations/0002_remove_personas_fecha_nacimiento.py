# Generated by Django 4.0.4 on 2022-06-02 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personas',
            name='fecha_nacimiento',
        ),
    ]
