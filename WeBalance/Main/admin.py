from django.contrib import admin

from .models import Preferences, WorkDone, Flagged

admin.site.register(Preferences)
admin.site.register(WorkDone)
admin.site.register(Flagged)