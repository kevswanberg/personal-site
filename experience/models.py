from django.db import models
from django.contrib.postgres.fields import DateTimeRangeField

class WorkExperience(models.Model):
    title = models.CharField(max_length=50)
    workplace = models.CharField(max_length=50)
    time_range = DateTimeRangeField()
    description = models.TextField()
