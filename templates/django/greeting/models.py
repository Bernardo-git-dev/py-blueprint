# greeting/models.py
from django.db import models

# Create your models here.
class Greeting(models.Model):
    message = models.CharField(max_length=200)
    recipient = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.message} to {self.recipient}"