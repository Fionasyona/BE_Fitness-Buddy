from django.db import models
from django.contrib.auth.models import User

# Profile Table 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)  
    height = models.FloatField(null=True, blank=True) 
    gender = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username

# Activity Table
class Activity(models.Model):
    ACTIVITY_CHOICES = [
        ('Running', 'Running'),
        ('Cycling', 'Cycling'),
        ('Weightlifting', 'Weightlifting'),
        ('Swimming', 'Swimming'),
        ('Walking', 'Walking'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    duration = models.PositiveIntegerField()  # minutes
    distance = models.FloatField(null=True, blank=True)  # km
    calories_burned = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.activity_type} - {self.user.username}"
