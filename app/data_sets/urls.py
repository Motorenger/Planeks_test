from django.urls import path

from data_sets.views import create_dataset, download_data_set

app_name = "data_sets"
urlpatterns = [
    path("create/<int:pk>", create_dataset, name="create"),
    path("download/<int:pk>", download_data_set, name="download")
]
