from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'index.html'


class LoginUserView(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('homepage')
    success_message = _('You are logged in successfully')

    def form_valid(self, form):
        return super().form_valid(form)


class LogoutUserView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)


def tk_handler_404(request, exception):
    return render(request=request, template_name='404.html', status=404)


def tk_handler_500(request):
    return render(request=request, template_name='500.html', status=500)
