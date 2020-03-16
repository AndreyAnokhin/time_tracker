from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, DeleteView

from .models import TimeTracking


class TimeTrackerView(LoginRequiredMixin, View):
    def get(self, request):
        projects = TimeTracking.objects.all()
        return render(request, 'time_tracker_site/time_tracking.html', context={'projects': projects})


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = TimeTracking
    fields = ['title', 'description', 'hours']
    template_name = 'time_tracker_site/add_task.html'
    success_url = reverse_lazy('time_tracker_url')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = TimeTracking
    success_url = reverse_lazy('time_tracker_url')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


def task_detail(request, task_id):
    task = get_object_or_404(TimeTracking, id=task_id)
    return render(request, 'time_tracker_site/task_detail.html', context={'task': task})
