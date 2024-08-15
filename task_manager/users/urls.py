from django.urls import path

from .views import (IndexView,
                    CreateUserView,
                    UpdateUserView,
                    DeleteUserView)


urlpatterns = [
    path('', IndexView.as_view(), name='users'),
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('<int:pk>/update/', UpdateUserView.as_view(), name='update_user'),
    path('<int:pk>/delete/', DeleteUserView.as_view(), name='delete_user'),
]
