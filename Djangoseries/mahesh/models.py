from django.db import models
from django.utils import timezone

# Create your models here.
class ComputerVarity(models.Model):
    COMPUTER_TYPE_CHOICES = [
        ('Laptop', 'Asus'),
        ('Desktop', 'Dell'),
        ('Mouse', 'Rog'),
        ('Keyboard', 'Logitech'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=100, choices=COMPUTER_TYPE_CHOICES)
    
    def __str__(self):
        return self.name