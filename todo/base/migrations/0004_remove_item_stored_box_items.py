# Generated by Django 4.0.4 on 2022-04-23 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_box_managers_alter_item_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='stored',
        ),
        migrations.AddField(
            model_name='box',
            name='items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boxed', to='base.item'),
        ),
    ]
