from django.urls import path
from .views import index, TimeTrackerView, TaskCreateView, task_detail, TaskDeleteView

urlpatterns = [
    path('', index, name='index_url'),
    path('time_tracker/', TimeTrackerView.as_view(), name='time_tracker_url'),
    path('add_task/', TaskCreateView.as_view(), name='add_task_url'),
    path('time_tracker/<int:task_id>/', task_detail, name='task_detail_url'),
    path('delete_task/<pk>/', TaskDeleteView.as_view(), name='task_delete_url'),
]
