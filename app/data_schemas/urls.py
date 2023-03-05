from django.urls import path

from data_schemas.views import (IndexView, DataSchemaCreate,
                                DataSchemaListView, DataSchemaDeleteView,
                                DataSchemaUpdate, DataSchemaDetailView
                            )


app_name = "data_schemas"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("schemas/", DataSchemaListView.as_view(), name="list"),
    path("schemas/create", DataSchemaCreate.as_view(), name="create"),
    path("schemas/detail/<int:pk>", DataSchemaDetailView.as_view(), name="detail"),
    path("schemas/update/<int:pk>", DataSchemaUpdate.as_view(), name="update"),
    path("schemas/delete/<int:pk>", DataSchemaDeleteView.as_view(), name="delete")
]
