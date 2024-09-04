from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from base.models import BaseModel, BaseModelName


model = get_user_model()


class Task(BaseModelName, BaseModel):

    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name=_('Description'))

    author = models.ForeignKey(model,
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

    executor = models.ForeignKey(model,
                                 null=True,
                                 blank=True,
                                 related_name='executor',
                                 on_delete=models.PROTECT,
                                 verbose_name=_('Executor'))

    labels = models.ManyToManyField(Label,
                                    blank=True,
                                    through='LabelAndTaskRelation',
                                    related_name='label',
                                    verbose_name=_('Labels'))

    def __str__(self):
        return self.name


class LabelAndTaskRelation(models.Model):
    """Model of relations between tasks and labels"""
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
