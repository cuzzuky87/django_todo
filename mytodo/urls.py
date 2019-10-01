from django.urls import path

from mytodo.views import list,detail,create,delete,update


app_name = 'mytodo'

urlpatterns = [
    path('',list.TaskListView.as_view(),name='task-list'),
    path('detail/<int:pk>/',detail.TaskDetailView.as_view(),name='task-detail'),
    path('create/',create.TaskCreateView.as_view(),name='task-create'),
    path('delete/<int:pk>/',delete.TaskDeleteView.as_view(),name='task-delete'),
    path('update/<int:pk>/',update.TaskUpdateView.as_view(),name='task-update'),
]