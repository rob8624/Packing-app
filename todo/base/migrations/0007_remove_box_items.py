# Generated by Django 4.0.4 on 2022-04-25 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_box_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='box',
            name='items',
        ),
    ]
