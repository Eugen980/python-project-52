from django.urls import path

from . import views


urlpatterns = [
    path('', views.UsersView.as_view(), name = 'users_list'),
    path('create/', views.RegisterUserView.as_view(), name = 'create_user'),
    path('<int:pk>/update/', views.UpdateUserView.as_view(), name = 'update_user'),
]
