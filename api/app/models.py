from django.db import models

class DateTime(models.Model):
    date = models.DateField(max_length=200)
    time = models.TimeField(max_length=200)