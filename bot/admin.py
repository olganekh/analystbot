from django.contrib import admin
from polls.models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    ...