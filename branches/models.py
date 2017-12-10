from django.db import models

# Create your models here.
class Section(models.Model):
    name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name

class TypeOfWork(models.Model):
    name = models.CharField(blank=True, max_length=100)
    section = models.ForeignKey(Section)
    
