from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    town = models.CharField(max_length=20)
    contact = models.IntegerField(max_length=16)
    price_range = models.FloatField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    #  created_by = models.ForeignKey()
    lat = models.DecimalField(max_digits=7, decimal_places=4)
    long = models.DecimalField(max_digits=7, decimal_places=4)

    def __str__(self):
        return self.name
