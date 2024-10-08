from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy

from task.forms import TaskForm
from task.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task:task-list")


class ToggleTaskCompletion(generic.UpdateView):

    model = Task
    fields = "__all__"

    def post(
            self,
            request: HttpRequest,
            *args: str,
            **kwargs: reverse_lazy
    ) -> HttpResponse:
        task_id = request.POST.get("task_id")
        task = Task.objects.get(id=task_id)

        task.is_completed = not task.is_completed
        task.save()

        return HttpResponseRedirect(
            reverse_lazy("task:task-list")
        )


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task:tag-list")
