from django.db import models
from career.validators import check_number_length, check_if_its_digits, phone_number_code_validator, name_validator

class ContactForm(models.Model):
    class Meta:
        verbose_name = 'Contact inquiry'
        verbose_name_plural = 'Contact inquiries'

    first_name = models.CharField(max_length=50,
                                  validators=[name_validator])
    last_name = models.CharField(max_length=50,
                                 validators=[name_validator])
    email = models.EmailField()
    phone_number = models.CharField(validators=[check_number_length,
                                         check_if_its_digits,
                                         phone_number_code_validator])
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)