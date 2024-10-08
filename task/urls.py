from django.urls import path

from task import views


urlpatterns = [
    path("", views.TaskListView.as_view(), name="task-list"),
    path("tasks/create/", views.TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/delete/",
        views.TaskDeleteView.as_view(),
        name="task-delete"
    ),
]

app_name = "task"
