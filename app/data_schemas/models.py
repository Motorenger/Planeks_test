from django.db import models
from django.utils.translation import gettext as _


class Arguments(models.Model):
    title = models.CharField(max_length=50)
    data_type = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class DataType(models.Model):
    title = models.CharField(max_length=50)
    extra_args = models.ManyToManyField(Arguments,  blank=True)

    def __str__(self):
        return self.title


class Column(models.Model):
    class DataTypes(models.TextChoices):
        MOVIE = 'MOVIE', 'Movie'
        SERIES = 'SERIES', 'Series'

    name = models.CharField(max_length=50)
    data_type = models.ForeignKey(DataType, on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        verbose_name = _('Column')
        verbose_name_plural = _('Columns')
        ordering = ['order']

    def __str__(self):
        return self.name


class DataSchema(models.Model):
    name = models.CharField(max_length=50)
    modified = models.DateField(auto_now=True)
    columns = models.ManyToManyField(Column)

    class Meta:
        verbose_name = _('DataSchema')
        verbose_name_plural = _('DataSchemas')
    
    def __str__(self):
        return self.name
