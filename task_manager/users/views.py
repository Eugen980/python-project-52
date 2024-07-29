
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, ListView

from .models import Users
from .forms import CreateUserForm



class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('home'))


class UsersView(ListView):
    template_name = 'users/users.html'
    model = Users
    context_object_name = 'users'


    def get_queryset(self):
        res =  Users.objects.order_by('-created_at')
        return res

class RegisterUserView(CreateView):
    template_name = 'users/create_user.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(**kwargs)
