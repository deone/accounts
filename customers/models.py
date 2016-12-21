from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

import random
import string

def generate_code(size=4, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

""" class Service(models.Model):
    pass """

class Customer(Group):
    # generate a randomized 4 digit code for customer
    code = models.CharField(_('name'), max_length=4, default=generate_code)

""" class CustomerUser(models.Model):
    user = models.OneToOneField(User)
    customer = models.ForeignKey(Customer)

class CustomerService(models.Model):
    customer = models.ForeignKey(Customer)
    service = models.ForeignKey(Service) """