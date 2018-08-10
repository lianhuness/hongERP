from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def isAdmin(self):
    return self.has_perm('auth.add_user')

def isSales(self):
    return self.has_perm('team.add_client')

# def isSalesMgr(self):
#     return self.has_perm('team.delete_client')

User.add_to_class("isAdmin",isAdmin)
User.add_to_class("isSales", isSales)
# User.add_to_class("isSalesManager", isSalesMgr)




