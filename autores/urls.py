from django.urls import path
from . import views

urlpatterns = [
    path("autores/", views.AutorCreateListView.as_view(), name="autor-create-list"),
]
