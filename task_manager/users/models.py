from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
# Create your models here.


class User(AbstractUser):

    first_name = models.CharField(max_length=150,
                                  verbose_name=_('First name'))

    last_name = models.CharField(max_length=150,
                                 verbose_name=_('Last name'))

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.get_full_name()
