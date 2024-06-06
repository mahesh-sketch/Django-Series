from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    description = models.TextField(default='No Description Available')    

    def __str__(self):
        return self.name
    
# One to Many relationship
class ComputerReview(models.Model): 
    computer = models.ForeignKey(ComputerVarity, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)
    comment = models.TextField(default='No Comment Available')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} rated {self.computer.name} {self.rating}'

#Many to Many relationship
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    computer_varieties = models.ManyToManyField(ComputerVarity,related_name='stores')

    def __str__(self):
        return self.name
    
#One to One 
class ComputerCertificate(models.Model):
    computer = models.OneToOneField(ComputerVarity, on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Certificate Number: {self.certificate_number} for {self.computer.name}'