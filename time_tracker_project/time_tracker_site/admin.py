from django.contrib import admin
from .models import TimeTracking


class TimeTrackingAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created',)


admin.site.register(TimeTracking, TimeTrackingAdmin)
