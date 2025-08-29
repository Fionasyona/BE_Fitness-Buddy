from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)  # in kg
    height = models.FloatField(blank=True, null=True)  # in cm
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Activity(models.Model):
    EXERCISE_CHOICES = [
        ('Push Ups', 'Push Ups'),
        ('Sit Ups', 'Sit Ups'),
        ('Squats', 'Squats'),
        ('Lunges', 'Lunges'),
        ('Plank', 'Plank'),
        ('Burpees', 'Burpees'),
        ('Jumping Jacks', 'Jumping Jacks'),
        ('Pull Ups', 'Pull Ups'),
        ('Bench Press', 'Bench Press'),
        ('Deadlift', 'Deadlift'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50, choices=EXERCISE_CHOICES, default= 'other') 
    duration_minutes = models.PositiveIntegerField()  # Duration in minutes
    reps = models.PositiveIntegerField(null=True, blank=True) 
    sets = models.PositiveIntegerField(null=True, blank=True)  # Optional
    calories = models.PositiveIntegerField(null=True, blank=True)
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.activity_type} by {self.user.username} on {self.date}"
