# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Hs Database(models.Model):

    #__Hs Database_FIELDS__
    manufacturer = models.TextField(max_length=255, null=True, blank=True)
    product name = models.TextField(max_length=255, null=True, blank=True)
    product description = models.TextField(max_length=255, null=True, blank=True)
    value = models.TextField(max_length=255, null=True, blank=True)
    shipment order number = models.TextField(max_length=255, null=True, blank=True)
    exporter = models.TextField(max_length=255, null=True, blank=True)
    country of origin = models.TextField(max_length=255, null=True, blank=True)

    #__Hs Database_FIELDS__END

    class Meta:
        verbose_name        = _("Hs Database")
        verbose_name_plural = _("Hs Database")



#__MODELS__END
