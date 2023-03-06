from django import forms

from data_sets.models import DataSet


class CreateDataSetForm(forms.Form):
    rows = forms.IntegerField()
