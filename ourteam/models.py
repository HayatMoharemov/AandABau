from django.db import models
from django.db.models import PROTECT

from career.models import JobPositions

class TeamMembersModel(models.Model):

    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'

    name = models.CharField(max_length=100)
    description = models.TextField()
    position = models.ForeignKey(JobPositions,
                                 on_delete=models.PROTECT,
                                 related_name='team_members')

    def __str__(self):
        return f"{self.name} - {self.position}"