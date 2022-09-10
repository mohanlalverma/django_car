from django.db import models

# Create your models here.


class Car(models.Model):

    STATUS_CHOICES = (
        ('bmw', 'BMW'),
        ('jaguar', 'JAGAUR'),
        ('toyota', 'TOYOTA'),
        ('audi', 'AUDI'),
        ('renaulT', 'RENAULT')
    )
    
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
