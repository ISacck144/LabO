
from django.db import models
from .Workload import Workload


class Announcement(models.Model):
    workload = models.ForeignKey(Workload, on_delete=models.CASCADE, related_name='announcements')
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.workload})"
