from django.db import models
import uuid

class YearCourse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=20, unique=True, null=True, blank=True)
    CURRICULUMS = [
        (2017, 'Plan 2017'),
        (2023, 'Plan 2023'),
    ]
    curriculum = models.IntegerField(choices=CURRICULUMS, default=2023)
    year = models.IntegerField(null=False)  # Año de carrera: 1, 2, 3, etc.
    name = models.CharField(max_length=100)  # Nombre personalizado para mostrar
    courses = models.ManyToManyField('Course', related_name='year_courses')
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('curriculum', 'year')
        ordering = ['curriculum', 'year']

    def __str__(self):
        return f"{self.name} ({self.get_curriculum_display()} - Año {self.year})"
