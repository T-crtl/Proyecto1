from django.db import models

# Create your models here.

class Name(models.Model):
    name_movie = models.CharField(max_length=200)
    description = models.TextField(max_length=255)
    image_url = models.CharField(max_length=255)
    pub_date = models.DateTimeField("Date published")

    def __str__(self):
        return f"{self.name_movie} {self.description}"
