from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


CRYPTO_LEVELS = [
    ('knows', _('Knows crypto')),
    ('newbie', _('Does not know crypto')),
]


class Profile(models.Model):
    user = models.OneToOneField('auth.User', related_name='profile')

    crypto_level = models.CharField(null=True, blank=True,
                                    choices=CRYPTO_LEVELS, max_length=20)

    keybase_username = models.CharField(null=True, blank=True, max_length=100)


@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    Profile.objects.get_or_create(
        user=instance,
    )
