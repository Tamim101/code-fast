from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=100)
    date = models.DateField()


    def __str__(self):
        return self.title
