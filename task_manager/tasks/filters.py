from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from task_manager.users.models import User


class TaskFilter(FilterSet):

    labels = ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_('Label'),
    )

    status = ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=_('Status'),
    )

    executor = ModelChoiceFilter(
        queryset=User.objects.all(),
        label=_('Executor'),
    )

    own_tasks = BooleanFilter(
        method='show_own_tasks',
        widget=forms.CheckboxInput(),
        required=False,
        label=_('Only my own tasks')
    )

    def show_own_tasks(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        else:
            return queryset

    class Meta:
        model = Task
        fields = ('status',
                  'executor',
                  'labels',
                  'own_tasks',
                  )
