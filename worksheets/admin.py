from django.contrib import admin
from worksheets.models import Worksheet, WorksheetFile

# Register your models here.
admin.site.register(Worksheet)
admin.site.register(WorksheetFile)
