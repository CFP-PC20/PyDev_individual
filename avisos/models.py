from django.db import models

# Create your models here.
class Project(models.Model):
    image = models.FilePathField(path="/img")