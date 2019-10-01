from django.views.generic import DetailView

from mytodo.models import Task


class TaskDetailView(DetailView):
    model = Task
    template_name = "mytodo/detail.html"