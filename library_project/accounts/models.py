from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from django.utils.translation import gettext as _
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(_('Phone Number'),max_length=11, unique=True)
    username = models.CharField(_('Username'),max_length=25)
    is_active = models.BooleanField(_('Active'), default=True)
    is_admin = models.BooleanField(_('Admin'), default=False)
    created_at = models.DateTimeField(_('Created At'),auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number

    @property
    def is_staff(self):
        return self.is_admin


class Otp(models.Model):
    phone_number = models.CharField(_('Phone Number'),max_length=11)
    code = models.PositiveSmallIntegerField(_('Code'))
    created_at = models.DateTimeField(_('Created At'),auto_now_add=True)

    class Meta:
        verbose_name = 'OTP'
        unique_together = ('phone_number', 'code')

    def __str__(self):
        return f'{self.phone_number} - {self.code}'

