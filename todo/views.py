from django.urls import  reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView

from .models import ToDo

# Create your views here.

class ToDoView(ListView):
    model = ToDo
    template_name = "todo/index.html"

class ToDoCreate(CreateView):
    model = ToDo
    fields = ["title"]
    template_name = "todo/addToDo.html"

    def get_context_data(self, **kwargs):
        context = super(ToDoCreate, self).get_context_data()
        context["title"] = "Add a new To Do"
        return context

class ToDoDelete(DeleteView):
    model = ToDo
    template_name = "todo/deleteToDo.html"

    success_url = reverse_lazy("index")
