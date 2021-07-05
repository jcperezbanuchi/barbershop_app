from django.db import models

# Create your models here.
class Appointment(models.Model):
  firstname = models.CharField(max_length=64)
  lastname = models.CharField(max_length=64)
  barber = models.CharField(max_length=64, blank=True, null=True)
  phone = models.CharField(max_length=12)
  email = models.EmailField(max_length=254, blank=True, null=True)
  contact = models.CharField(max_length=64, blank=True, null=True)
  date = models.DateField()
  time = models.CharField(max_length=64)
  comment = models.TextField(blank=True, null=True)

  def __str__(self):
    return f"{self.firstname}, {self.lastname},{self.barber},{self.phone},{self.email},{self.contact},{self.date},{self.time}, {self.comment}"
