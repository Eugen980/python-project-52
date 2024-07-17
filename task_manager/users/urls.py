from django.urls import path

from .views import UsersView, RegisterUserView


urlpatterns = [
    path('', UsersView.as_view(), name = 'users_list'),
    path('create/', RegisterUserView.as_view(), name = 'create_user'),
]
