from django.db import models
from django.utils.translation import gettext as _

from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class Task(models.Model):

    name = models.CharField(max_length=100,
                            unique=True,
                            verbose_name=_('Name'))

    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name=_('Description'))

    author = models.ForeignKey(User,
                               null=True,
                               related_name='author',
                               on_delete=models.PROTECT,
                               verbose_name=_('Author'))

    status = models.ForeignKey(Status,
                               on_delete=models.PROTECT,
                               null=True,
                               blank=True,
                               related_name='status',
                               verbose_name=_('Status'))

    executor = models.ForeignKey(User,
                                 null=True,
                                 blank=True,
                                 related_name='executor',
                                 on_delete=models.PROTECT,
                                 verbose_name=_('Executor'))

    created_at = models.DateTimeField(auto_now_add=True)

    labels = models.ManyToManyField(Label,
                                    blank=True,
                                    through='LabelAndTaskRelation',
                                    related_name='label',
                                    verbose_name=_('Labels'))

    def __str__(self):
        return self.name


class LabelAndTaskRelation(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
