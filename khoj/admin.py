
from django.contrib import admin
from .models import InputRecord


class InputRecordAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'input_values')


admin.site.register(InputRecord, InputRecordAdmin)
