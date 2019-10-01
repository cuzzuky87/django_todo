from django.views.generic import UpdateView
from django.urls import reverse_lazy

from mytodo.models import Task


class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'mytodo/update.html'
    success_url = reverse_lazy('mytodo:task-list')