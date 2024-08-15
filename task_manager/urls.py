from django.contrib import admin
from django.urls import path, include

from .views import HomeView, LoginUserView, LogoutUserView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('labels/', include('task_manager.labels.urls')),
]

handler404 = 'task_manager.views.tk_handler_404'
handler500 = 'task_manager.views.tk_handler_500'
