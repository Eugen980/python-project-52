from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from .models import Label
from .forms import LabelForm
from task_manager.mixins import DeleteProtectionMixin


class IndexLabelView(ListView):
    model = Label
    template_name = 'labels/index.html'
    context_object_name = 'labels'

    def get_queryset(self):
        return Label.objects.all()


class CreateLabelView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels')
    success_message = _('Label was created successfully')
    login_url = reverse_lazy('login')


class UpdateLabelView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels')
    success_message = _('Label was updated successfully')
    login_url = reverse_lazy('login')


class DeleteLabelView(DeleteProtectionMixin,
                      LoginRequiredMixin,
                      SuccessMessageMixin,
                      DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels')
    success_message = _('Label was deleted successfully')
    login_url = reverse_lazy('login')
    protected_message = _('''It is not possible to delete this label,
     because it is related to tasks''')
    protected_url = reverse_lazy('labels')
