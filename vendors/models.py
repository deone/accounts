from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Vendor(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.CharField(max_length=10)
    company_name = models.CharField(max_length=50)
    
    def __str__(self):
        return '%s, %s' % (self.user.get_full_name(), self.company_name)
    
    def to_dict(self):
        return {
            'vendor_id': self.pk,
            'name': self.user.get_full_name(),
            'phone_number': self.phone_number,
            'company_name': self.company_name
        }