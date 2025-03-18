from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    is_member = models.BooleanField(default=True)

from django.db import models

class Consultation(models.Model):
    patient_name = models.CharField(max_length=255)
    mrn = models.CharField(max_length=20)
    consult_type = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.patient_name} ({self.mrn}) - {self.consult_type}"