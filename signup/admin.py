from django.contrib import admin

from .models import Attendee


class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'want_to_know', 'can_help_with')


admin.site.register(Attendee, AttendeeAdmin)
