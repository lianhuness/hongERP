from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def isAdmin(self):
    return self.has_perm('auth.add_user')

User.add_to_class("isAdmin",isAdmin)
