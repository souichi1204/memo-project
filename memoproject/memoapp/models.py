from cgitb import text
from django.db import models

# Create your models here.
class Memomodel(models.Model):
  タイトル=models.CharField(max_length=100)
  本文=models.TextField()

      
  def __str__(self):
        return self.タイトル