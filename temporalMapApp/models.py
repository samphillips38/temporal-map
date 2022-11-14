from django.db import models

# Create your models here.
class Map(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    coords = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.title