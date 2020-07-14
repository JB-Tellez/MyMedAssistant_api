from django.db import models
import importlib.util

from user.models import User
from medication.models import Medication

class Scheduler(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
  hours = models.IntegerField()
  dosage = models.CharField(max_length=256)
  start = models.DateTimeField(auto_now=False, auto_now_add=False)
  next_dosage = models.DateTimeField(auto_now=False, auto_now_add=False)
  end = models.DateTimeField(auto_now=False, auto_now_add=False)
  user_id_medication = models.CharField(max_length=64)

  def __str___(self):
    return self.user_id_medication
