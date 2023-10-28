from django.db import models


class Music(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.pk} - Instrument: {self.name} - and {self.description} - providing {self.teacher} and for 45 minutes cost only {self.price}$"


