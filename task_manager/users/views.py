from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

from .models import Users


class UsersView(View):

    def get(self, request, *args, **kwargs):
        users = Users.objects.order_by('-created_at')
        return render(request, 'users/users.html', {'users':users})


class RegisterUserView(CreateView):
    template_name = 'users/create_user.html'
    model = Users
    form_class = UserCreationForm
    success_url = reverse_lazy('users_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(**kwargs)
