from django.urls import path

from .views import (IndexTaskView,
                    CreateTaskView,
                    UpdateTaskView,
                    DeleteTaskView,
                    ShowTaskView)

urlpatterns = [
    path('', IndexTaskView.as_view(), name='tasks'),
    path('create/', CreateTaskView.as_view(), name='task_create'),
    path('<int:pk>/update/', UpdateTaskView.as_view(), name='task_update'),
    path('<int:pk>/delete/', DeleteTaskView.as_view(), name='task_delete'),
    path('<int:pk>/', ShowTaskView.as_view(), name='task_show'),
]
