from django import forms
from data_schemas.models import DataSchema, Column, DataType


class DataSchemaForm(forms.ModelForm):
    class Meta:
        model = DataSchema
        fields = ('name', 'columns')

    name = forms.CharField()
    columns = forms.ModelMultipleChoiceField(
        queryset=DataType.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
