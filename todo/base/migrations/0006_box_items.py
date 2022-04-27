# Generated by Django 4.0.4 on 2022-04-25 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_box_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='box', to='base.item'),
        ),
    ]
