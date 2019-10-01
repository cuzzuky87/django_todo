from django.views.generic import DeleteView
from django.urls import reverse_lazy

from mytodo.models import Task


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'mytodo/delete.html'
    success_url = reverse_lazy('mytodo:task-list')