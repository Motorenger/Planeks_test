from django.urls import path

from data_schemas.views import IndexView, ContactFormView


app_name = "data_schemas"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("schemas/create", ContactFormView.as_view(), name="create")
]
