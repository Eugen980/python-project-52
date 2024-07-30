from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import logout


class HomeView(TemplateView):
    template_name = 'index.html'


class LoginUserView(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    success_message = 'Вы залогинены'

    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        return super().get_success_message(cleaned_data)



def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('home'))
