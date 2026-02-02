from django.core.exceptions import ValidationError


def phone_number_code_validator(value):
    if not value.startswith('+49'):
        raise ValidationError('Your phone number must start with +49!')


def check_if_its_digits(value):
    value = value[1:]
    try:
        int(value)
    except ValueError:
        raise ValidationError('Phone number must be only digits!')


def check_number_length(value):
    value = value[3:]
    if not 10 <= len(value) <= 11:
        raise ValidationError('Phone number must be 12 or 13 digits!')


def name_validator(value):
    allowed_chars = set("'- ")
    for char in value:
        if not (char.isalpha() or char in allowed_chars):
            raise ValidationError('Name can contain only letters, spaces, hyphens and apostrophes!')
