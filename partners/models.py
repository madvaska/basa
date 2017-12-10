from django.db import models

# Create your models here.
class Partner(models.Model):
    INN = models.BigIntegerField()
    email = models.EmailField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
