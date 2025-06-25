from django.db import models
from django.utils.translation import gettext_lazy as _

class Proxy(models.Model):
    # ID automático (por defecto, Django agrega un campo id autoincremental)
    names = models.CharField(max_length=150, null=False, blank=False)
    father_surname = models.CharField(max_length=100, null=False, blank=False)
    mother_surname = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['names', 'father_surname', 'mother_surname']

    def save(self, *args, **kwargs):
        self.names = self.names.upper()
        self.father_surname = self.father_surname.upper()
        self.mother_surname = self.mother_surname.upper()
        super(Proxy, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.names} {self.father_surname} {self.mother_surname}"
