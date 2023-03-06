from django.db import models

from data_schemas.models import DataSchema


class DataSet(models.Model):
    created = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)
    schema = models.ForeignKey(DataSchema, on_delete=models.CASCADE, related_name="data_sets")
    data_set_path = models.TextField()
