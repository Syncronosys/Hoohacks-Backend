from django.contrib import admin
from . import models


class AdminSession(admin.ModelAdmin):
    pass


class AdminClient(admin.ModelAdmin):
    pass


admin.site.register(models.Client, AdminClient)
admin.site.register(models.Session, AdminSession)
