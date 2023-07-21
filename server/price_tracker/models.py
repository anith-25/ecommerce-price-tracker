from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=350)
    url = models.URLField(max_length=1000)
    image = models.ImageField(upload_to="images/", max_length=500)
    initial_price = models.PositiveIntegerField()
    current_price = models.PositiveIntegerField()
    cuttoff_price = models.PositiveIntegerField(null=True, blank=True)
    amount_discount = models.IntegerField(default=0)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
