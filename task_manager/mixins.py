from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import ProtectedError
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class CustomLoginRequiredMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        messages.error(self.request,
                       _('You are not logged in! Please log in.'))
        return redirect(reverse('login'))


class LoginRequiredAndUserSelfCheckMixin(CustomLoginRequiredMixin,
                                         UserPassesTestMixin):
    def test_func(self):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        else:
            messages.error(
                self.request,
                _('You do not have permission to modify another user.'))
            return redirect('user_list')


class DeleteProtectionMixin:
    protected_message = None
    protected_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)


class TaskDeleteProtection(UserPassesTestMixin):
    author_message = None
    author_url = None

    def test_func(self):
        return self.get_object().author == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.author_message)
        return redirect(self.author_url)
