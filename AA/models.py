
from django.db import models

class Human(models.Model):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]

    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25,null=True,blank=True)
    age = models.PositiveIntegerField(default=50)
    gender = models.CharField(max_length=6, choices=GENDER,null=True,blank=True)
    image = models.ImageField(upload_to='images/', default='def.jpg')  # Set your default image path
    address = models.TextField(max_length=400,null=True,blank=True)

    def str(self):
        return self.name