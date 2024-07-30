from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse

from .models import Users
from .forms import CreateUserForm, UpdateUserForm


class UsersView(ListView):
    template_name = 'users/users.html'
    model = get_user_model()
    context_object_name = 'users'


    def get_queryset(self):
        res =  Users.objects.order_by('-created_at')
        return res

class RegisterUserView(CreateView):
    template_name = 'users/form_user.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    extra_context = {
        'title': 'Регистрация',
        }

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(**kwargs)





class UpdateUserView(UpdateView):
    template_name = 'users/form_user.html'
    model = get_user_model()
    form_class = UpdateUserForm
    success_url = reverse_lazy('users_list')
