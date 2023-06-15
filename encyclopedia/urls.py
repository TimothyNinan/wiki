from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("CreateNewPage",  views.create, name="create"),
    path("EditPage", views.edit, name="edit"),
    path("Random", views.random, name="random"),
    path("<str:title>", views.page, name="page")
]
