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
    path(
        "tasks/<int:pk>/update/",
        views.TaskUpdateView.as_view(),
        name="task-update"
    ),
    path("tags/", views.TagListView.as_view(), name="tag-list"),
    path("tags/create/", views.TagCreateView.as_view(), name="tag-create"),
]

app_name = "task"
