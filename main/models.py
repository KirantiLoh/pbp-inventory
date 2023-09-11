from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    # price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField()
    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.name