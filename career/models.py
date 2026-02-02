from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now

from common.validators import phone_number_code_validator, check_if_its_digits, check_number_length, name_validator


class JobPositions(models.Model):

    class Meta:
        verbose_name = 'Job Position'
        verbose_name_plural = 'Job Positions'

    class EmploymentChoices(models.TextChoices):
        FULL_TIME = 'full_time', 'Full Time',
        PART_TIME = 'part_time', 'Part Time',
        CONTRACT = 'contract', 'Contract'

    class TitleChoices(models.TextChoices):
        SITE_SUPERVISOR = 'site_supervisor', 'Site Supervisor',
        TECHNICAL_MANAGER = 'technical_manager', 'Technical Manager',
        CONSTRUCTION_WORKER = 'construction_worker', 'Construction Worker'
        OFFICE_ADMINISTRATOR = 'office_administrator', 'Office Administrator'

    title = models.CharField(max_length=200,
                             choices=TitleChoices)
    slug = models.SlugField(unique=True,
                            editable=False)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    location = models.CharField(max_length=50)
    employment_type = models.CharField(max_length=50,
                                       choices=EmploymentChoices,
                                       default=EmploymentChoices.FULL_TIME)
    date_posted = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{now()}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class JobApplication(models.Model):

    class Meta:
        verbose_name = 'Job Application'
        verbose_name_plural = 'Job Applications'

    class HireChoices(models.TextChoices):
        HIRED = 'Hired', 'Hired'
        NOT_HIRED = 'Not hired', 'Not hired'

    job = models.ForeignKey(JobPositions,
                            on_delete=models.CASCADE,
                            related_name='position')
    first_name = models.CharField(max_length=100,
                                  validators=[name_validator])
    last_name = models.CharField(max_length=100,
                                   validators=[name_validator])
    email = models.EmailField()
    phone_number = models.CharField(max_length=14,
                             validators=[check_number_length,
                                         check_if_its_digits,
                                         phone_number_code_validator])
    cover_letter = models.TextField(blank=True,
                           null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_hired = models.CharField(max_length=20,
                                choices=HireChoices,
                                default=HireChoices.NOT_HIRED)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job.title}"
