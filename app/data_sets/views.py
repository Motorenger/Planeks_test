import mimetypes

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from data_sets.models import DataSet
from data_sets.tasks import get_season_data
from data_schemas.models import DataSchema

def create_dataset(request, pk, *args, **kwargs):

    if request.method == "POST":
        rows = request.POST.get("rows")
        schema = get_object_or_404(DataSchema, pk=pk)
        if rows:
            data_set = DataSet(schema=schema)
            data_set.save()
        columns = [{"name": column.name, "data_type": column.data_type.title} for column in schema.columns.all()]

        get_season_data.delay(data_set_pk=data_set.pk, columns=columns, rows=rows)   
    return redirect('data_schemas:detail', pk=pk)


def download_data_set(request, pk):

    data_set = get_object_or_404(DataSet, pk=pk)

    with open(data_set.data_set_path, 'r') as f:
        mime_type, _ = mimetypes.guess_type(data_set.data_set_path)
        response = HttpResponse(f, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=data_set.csv"
        return response
