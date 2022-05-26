from cgitb import text
from django.db import models
from django.utils import timezone

# Create your models here.
class Memomodel(models.Model):
  タイトル=models.CharField(max_length=100)
  本文=models.TextField()
  作成した日付=models.DateTimeField(default=timezone.now)

      
  def __str__(self):
        return self.タイトル