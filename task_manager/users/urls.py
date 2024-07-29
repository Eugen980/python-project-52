from django.urls import path

from . import views


urlpatterns = [
    path('', views.UsersView.as_view(), name = 'users_list'),
    path('create/', views.RegisterUserView.as_view(), name = 'create_user'),
    path('logout/', views.logout_user, name = 'logout'),
    path('login/', views.LoginUserView.as_view(), name = 'login')
]
