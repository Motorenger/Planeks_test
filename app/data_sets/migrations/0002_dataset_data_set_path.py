# Generated by Django 4.1.7 on 2023-03-06 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_sets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='data_set_path',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]