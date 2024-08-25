from django.utils.translation import gettext as _
from base.models import BaseModel, BaseModelName


class Label(BaseModel, BaseModelName):
    class Meta:
        verbose_name = _('Label')
        verbose_name_plural = _('Labels')
        ordering = ['-created']
