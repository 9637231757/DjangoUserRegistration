from django.db import models

# Create your models here.
        
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to ='photos/', blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    
    def __str__(self):
        return self.name        