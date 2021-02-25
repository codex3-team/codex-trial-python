import uuid

from django.db import models


class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    year = models.IntegerField()

    class Meta:
        ordering = ['-make']

    def __str__(self):
        return f"car {self.make}/{self.model}/{self.year}"
