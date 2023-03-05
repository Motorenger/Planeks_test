from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView

from data_schemas.forms import DataSchemaForm, ColumnFormSet
from data_schemas.models import DataSchema


class IndexView(TemplateView):
    template_name = 'data_schemas/index.html'


class DataSchemaListView(ListView):
    model = DataSchema
    template_name = 'data_schemas/list_schemas.html'
    context_object_name = 'schemas'


class DataSchemaDetailView(DetailView):
    model = DataSchema
    template_name = 'data_schemas/detail_schema.html'
    context_object_name = 'schema'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["columns"] = self.object.columns.select_related() 
        context["data_sets"] = self.object.data_sets.all() 
        return context


class DataSchemaDeleteView(DeleteView):
    model = DataSchema
    template_name = 'data_schemas/delete_schema.html'
    success_url = reverse_lazy('data_schemas:list')


class DataSchemaInline():
    form_class = DataSchemaForm
    model = DataSchema
    template_name = "data_schemas/create_schema.html"

    def form_valid(self, form):
        column_formset = self.get_column_formset()
        if not column_formset.is_valid():
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        formset_save_func = getattr(self, 'formset_columns_valid', None)
        if formset_save_func is not None:
            formset_save_func(column_formset)
        else:
            column_formset.save()
        return redirect('data_schemas:index')

    def formset_columns_valid(self, formset):
        """
        Hook for custom formset saving.Useful if you have multiple formsets
        """
        columns = formset.save(commit=False)

        for column in columns:
            column.schema = self.object
            column.save()


class DataSchemaCreate(DataSchemaInline, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(DataSchemaCreate, self).get_context_data(**kwargs)
        ctx['columns_formset'] = self.get_column_formset()
        return ctx

    def get_column_formset(self):
        if self.request.method == "GET":
            return ColumnFormSet(prefix='columns')
        else:
            return ColumnFormSet(self.request.POST or None, prefix='columns')


class DataSchemaUpdate(DataSchemaInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(DataSchemaUpdate, self).get_context_data(**kwargs)
        ctx['columns_formset'] = self.get_column_formset()
        return ctx

    def get_column_formset(self):
        return ColumnFormSet(self.request.POST or None, instance=self.object, prefix='columns'),
