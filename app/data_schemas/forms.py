from django import forms
from django.forms import inlineformset_factory

from data_schemas.models import DataSchema, Column


class DataSchemaForm(forms.ModelForm):

    class Meta:
        model = DataSchema
        exclude = ("modified",)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
        }


class ColumnForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ColumnForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Column
        exclude = ('schema',)
        widgets = {
            'name': forms.TextInput(),
            'order': forms.NumberInput(),
        }


ColumnFormSet = inlineformset_factory(
    DataSchema, Column, form=ColumnForm,
    extra=1, can_delete=False, can_delete_extra=False
)
