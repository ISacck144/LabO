from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

from .Course import Course
from .Teacher import Teacher
from .YearCourse import YearCourse

class Workload(models.Model):
    year_course = models.ForeignKey(YearCourse, null=True, on_delete=models.CASCADE)
    group = models.CharField(max_length=1, choices=[('U', 'Único')], default='U')
    capacity = models.PositiveIntegerField(default=20)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('year_course', 'group')
        ordering = ['year_course', 'group']

    def __str__(self):
        return f"{self.year_course} - Grupo {self.group} - {self.teacher}"