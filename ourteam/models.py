from django.db import models
from django.utils.text import slugify

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
    date_joined = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):

        if not self.slug:
            date_str = self.date_joined.strftime('%d-%m-%y')
            self.slug = slugify(f"{self.name}-{self.position}-{date_str}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.position}"