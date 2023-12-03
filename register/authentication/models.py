from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _



# Create your models here.
def validate_username(value):
    if not value.startswith('@'):
        raise ValidationError(_("Username must start with '@'"))

class User(models.Model):
    # Other fields...

    username = models.CharField(
        max_length=100,
        unique=True,
        validators=[validate_username],
        # Other options...
    )

    # Other fields...
