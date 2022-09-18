from django.contrib import admin

from Account.models import Account, Profile

# Register your models here.
admin.site.register(Account)
admin.site.register(Profile)