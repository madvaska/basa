from django.db import models

# Create your models here.
class Partner(models.Model):
    INN = models.BigIntegerField()
    email = models.EmailField()
    name = models.CharField()

    def __str__(self):
        return self.name
    
