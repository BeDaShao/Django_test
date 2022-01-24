from django.db import models

# Create your models here.
class Link(models.Model):
    code = models.CharField(max_length=255)
    url = models.URLField()
