from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    age=models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(80)],
                                           null=True, blank=True)
    status_choices = (
    ('client', 'client'),
    ('owner', 'owner'),
    )
    status = models.CharField(choices=status_choices,default='client', max_length=20)
    phone_number=PhoneNumberField(null=True, blank=True)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username}'