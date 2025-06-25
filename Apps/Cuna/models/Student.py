from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from .Proxy import Proxy

class Student(models.Model):
    cui = models.IntegerField(unique=True, null=True, blank=True)
    names = models.CharField(null=False, blank=False, max_length=155)
    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)

    proxy = models.ForeignKey(Proxy, on_delete=models.SET_NULL, null=True, related_name='students')


    class Meta:
        ordering = ['cui', 'names']

    def save(self, *args, **kwargs):
        self.names = self.names.upper()
        return super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.cui} {self.names}"

