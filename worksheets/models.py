from django.db import models
from branches.models import TypeOfWork
from partners.models import Partner
from datetime import datetime

# Create your models here.
class Worksheet(models.Model):
    partner = models.ForeignKey(Partner)
    typeOfWork = models.ForeignKey(TypeOfWork)
    importdatetime = models.DateTimeField(blank=True, default=datetime.now)
    comment = models.TextField(blank=True)
    originalFile = models.ForeignKey(WorksheetFile)

    def __str__(self):
        return self.partner.name+self.typeOfWork.name

class WorksheetFile(models.Model):
    original = models.FileField(upload_to='uploads')
    fileName = models.CharField(max_length=255, unique = True)
