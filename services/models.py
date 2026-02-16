from django.db import models

from ourteam.models import TeamMembersModel

class ServicesTypeModel(models.Model):

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    class ServiceTypeChoices(models.TextChoices):
        FACADE_WORKS = 'Facade Works', 'Facade Works'
        INSULATION = 'Insulation', 'Insulation'
        PLASTERING = 'Plastering', 'Plastering'
        RENOVATION = 'Renovation', 'Renovation'
        ROOF_REPAIR = 'Roof Repair', 'Roof Repair'
        SEWER_CONSTRUCTION = 'Sewer Construction', 'Sewer Construction'


    type = models.CharField(max_length=50,
                            choices=ServiceTypeChoices.choices)
    short_description = models.TextField()
    description = models.TextField()
    overview_image = models.ImageField(upload_to='static/images/services')
    detail_view_image = models.ImageField(upload_to='static/images/services')
    responsible_person = models.ManyToManyField(TeamMembersModel,
                                                related_name='services')

    def __str__(self):
        return f"{self.type}"