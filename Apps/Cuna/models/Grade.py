from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .Inscription import Inscription
from .YearCourse import YearCourse

class Grade(models.Model):
    EVALUATION_TYPES = [
        ('EXAM', 'Examen'),
        ('PRACTICE', 'Práctica'),
        ('HOMEWORK', 'Tarea'),
        ('PROJECT', 'Proyecto'),
        ('PARTICIPATION', 'Participación'),
        ('FINAL', 'Nota Final'),
    ]
    
    inscription = models.ForeignKey(
        Inscription, 
        on_delete=models.CASCADE, 
        related_name='grades'
    )
    evaluation_type = models.CharField(
        max_length=20, 
        choices=EVALUATION_TYPES,
        default='EXAM'
    )
    score = models.DecimalField(
        max_digits=4, 
        decimal_places=2,
        validators=[
            MinValueValidator(0.00),
            MaxValueValidator(20.00)
        ]
    )
    max_score = models.DecimalField(
        max_digits=4, 
        decimal_places=2,
        default=20.00
    )
    description = models.CharField(max_length=200, blank=True, null=True)
    evaluation_date = models.DateField()
    weight = models.DecimalField(
        max_digits=3, 
        decimal_places=2,
        default=1.00,
        help_text="Peso de la evaluación para el promedio"
    )
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['inscription', 'evaluation_date', 'evaluation_type']
        unique_together = ['inscription', 'evaluation_type', 'description']

    def __str__(self):
        return f"{self.inscription.student.names} - {self.get_evaluation_type_display()}: {self.score}"

    @property
    def percentage_score(self):
        """Convierte la nota a porcentaje"""
        return (self.score / self.max_score) * 100 if self.max_score > 0 else 0