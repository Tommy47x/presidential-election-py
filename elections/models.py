from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    party = models.CharField(max_length=200)
    image_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
