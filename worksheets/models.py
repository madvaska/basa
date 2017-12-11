from django.db import models
from branches.models import TypeOfWork
from partners.models import Partner
from datetime import datetime

# Create your models here.
class WorksheetFile(models.Model):
    original = models.FileField(upload_to='uploads')
    fileName = models.CharField(max_length=255, unique = True)

class Worksheet(models.Model):
    partner = models.ForeignKey(Partner)
    typeOfWork = models.ForeignKey(TypeOfWork)
    importdatetime = models.DateTimeField(blank=True, default=datetime.now)
    comment = models.TextField(blank=True)
    originalFile = models.ForeignKey(WorksheetFile, blank = True, default = None)

    def __str__(self):
        return self.partner.name+self.typeOfWork.name
