from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from data_schemas.forms import DataSchemaForm
from data_schemas.models import DataSchema


class IndexView(TemplateView):
    template_name = 'data_schemas/index.html'


class ContactFormView(CreateView):
    model = DataSchema
    template_name = 'data_schemas/create_schema.html'
    form_class = DataSchemaForm
    success_url = 'data_schemas:index'
