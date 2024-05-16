from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    party = models.CharField(max_length=200)
    image_url = models.URLField(max_length=200)
    votes = models.IntegerField(default=0)  # new field
    description = models.TextField(default ='')  # new field
    party_image_url = models.URLField(max_length=200, default ='')  # new field

    def __str__(self):
        return self.name

# Create your models here.
