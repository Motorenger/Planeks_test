# Generated by Django 4.1.7 on 2023-03-05 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_schemas', '0005_remove_dataschema_columns_column_schema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='data_schemas.dataschema'),
        ),
    ]
