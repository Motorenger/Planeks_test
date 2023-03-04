from django.urls import path

from data_schemas.views import IndexView


app_name = "data_schemas"
urlpatterns = [
    path("", IndexView.as_view(), name="index")
]
