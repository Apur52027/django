from django.db import models

# Create your models here.
class adminform(models.Model):
  auto_field = models.AutoField(primary_key=True)
  char_field = models.CharField(max_length=255)
  boolean_field = models.BooleanField()
  date_field = models.DateField()
  decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
  duration_field = models.DurationField()
  email_field = models.EmailField()
  file_field = models.FileField(upload_to='files/')
  date_time_field = models.DateTimeField()
  