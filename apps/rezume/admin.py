from django.contrib import admin

from rezume.models import (
    File,
    Resume
)

class FileAdmin(admin.ModelAdmin):
    readonly_fields =()

class ResumeAdmin(admin.ModelAdmin):

    redonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )
admin.site.register(
    File, FileAdmin
)
admin.site.register(
    Resume, ResumeAdmin
)