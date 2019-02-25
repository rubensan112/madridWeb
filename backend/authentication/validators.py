from django.core.exceptions import ValidationError


def username_validator(value):
    valid_username_characters = 'abcdefghijklmnñopqrstuvwxyz0123456789.-_'

    if not all(elem in valid_username_characters for elem in value.lower()):
        raise ValidationError('\'{0}\' value is not correct for username'.format(
            value
        ))
