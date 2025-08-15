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
    ACTIVITY_CHOICES = [
        ('Running', 'Running'),
        ('Cycling', 'Cycling'),
        ('Weightlifting', 'Weightlifting'),
        ('Swimming', 'Swimming'),
        ('Walking', 'Walking'),
        ('Yoga', 'Yoga'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    duration_minutes = models.PositiveIntegerField()  # Duration in minutes
    distance_km = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # Optional
    calories_burned = models.PositiveIntegerField(null=True, blank=True)
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)  # Track creation time
    updated_at = models.DateTimeField(auto_now=True)      # Track update time

    class Meta:
        ordering = ['-date', '-created_at']  # Default sorting: newest first

    def __str__(self):
        return f"{self.activity_type} by {self.user.username} on {self.date}"
