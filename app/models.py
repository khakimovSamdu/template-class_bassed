from django.db import models

# Create your models here.
class Smartphones(models.Model):
    name = models.CharField(max_length = 64)
    company = models.CharField(max_length = 46)
    color = models.CharField(max_length = 48)
    RAM = models.CharField(max_length = 24)
    memory = models.CharField(max_length = 36)
    price = models.FloatField()
    img_url = models.CharField(max_length = 98)

    def __str__(self) -> str:
        return self.name
    