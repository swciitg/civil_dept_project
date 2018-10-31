from django.contrib import admin
from . import models

from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.Staff)
admin.site.register(models.Hod)
admin.site.register(models.Dppc)
admin.site.register(models.ApplyLeave)
admin.site.register(models.Comments)


class UserAdmin(UserAdmin):
    pass

admin.site.register(models.User , UserAdmin)
