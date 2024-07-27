from django.db import models

class Alert(models.Model):
    email = models.EmailField()
    price = models.DecimalField(max_digits=20, decimal_places=10)
    title = models.CharField(max_length=100, default='Bitcoin') 
