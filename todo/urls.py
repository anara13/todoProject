from django.urls import path
from . import views


urlpatterns = [
    path("", views.ToDoView.as_view(), name="index"),
    path("addToDo/", views.ToDoCreate.as_view(), name="add-To-Do"),
]