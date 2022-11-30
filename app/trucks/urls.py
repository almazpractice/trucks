from django.urls import path

from .views import TrucksView


app_name = "trucks"


urlpatterns = [
    path("", TrucksView.as_view(), name="main"),
]
