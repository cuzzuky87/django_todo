from django.views.generic import ListView

from mytodo.models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'mytodo/list.html'