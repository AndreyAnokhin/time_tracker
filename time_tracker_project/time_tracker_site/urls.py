from django.urls import path
from .views import index, TimeTrackerView, TaskCreateView

urlpatterns = [
    path('', index, name='index_url'),
    path('time_tracker/', TimeTrackerView.as_view(), name='time_tracker_url'),
    path('add_task/', TaskCreateView.as_view(), name='add_task_url'),
]
