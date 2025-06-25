from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(unique=True, null=True, blank=True, max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    credits = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=2)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(null=False, blank=False, max_length=255)
    bimester = models.IntegerField(null=False, default=1)
    status = models.BooleanField(default=True)
    year = models.IntegerField(null=False, default=1)

    def __str__(self):
        return f"{self.code} - {self.name}"