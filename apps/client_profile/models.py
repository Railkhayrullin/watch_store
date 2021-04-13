from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='client_profile', on_delete=models.CASCADE)
    phone = models.CharField('phone', max_length=20, blank=False)
    is_active = models.BooleanField('is_active', default=True)

    def __str__(self):
        return str(self.user.username) + ' | ' + str(self.user.email)

    class Meta:
        verbose_name = 'client_profile'
        verbose_name_plural = 'clients_profile'

    def email(self):
        return self.user.email
