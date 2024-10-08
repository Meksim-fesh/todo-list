from django.urls import path

from task import views


urlpatterns = [
    path("", views.TaskListView.as_view(), name="task-list"),
    path("tasks/create/", views.TaskCreateView.as_view(), name="task-create"),
]

app_name = "task"
