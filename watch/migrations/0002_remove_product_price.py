# Generated by Django 3.1.7 on 2021-04-07 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
