from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import CreateView

from .models import ToDo

# Create your views here.

class ToDoView(ListView):
    model = ToDo
    template_name = "todo/index.html"

class ToDoCreate(CreateView):
    model = ToDo
    fields = ["title"]
    template_name = "todo/addToDo.html"

    def get_context_data(self):
        context = super(ToDoCreate, self).get_context_data()
        context["title"] = "Add a new ToDo"
        return context
