from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid

class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    make = models.CharField(_('Make'), max_length=128)
    model = models.CharField(_('Model'), max_length=128)
    year = models.CharField(_('Year'), max_length=4)


    class Meta:
        ordering = ['-year']
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')
