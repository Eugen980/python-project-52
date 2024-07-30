
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('users/', include('task_manager.users.urls')),
    path('admin/', admin.site.urls),
    path('logout/', views.logout_user, name = 'logout'),
    path('login/', views.LoginUserView.as_view(), name = 'login')
]
