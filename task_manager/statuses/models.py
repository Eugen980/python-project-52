from django.utils.translation import gettext as _
from base.models import BaseModel, BaseModelName


class Status(BaseModel, BaseModelName):
    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')
        ordering = ['-created']
