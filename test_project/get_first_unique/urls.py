from django.urls import path

from get_first_unique import views

urlpatterns = [
    path("", views.index, name="index"),
    path("result/", views.result, name="result"),
]
