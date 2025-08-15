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
        ("Running", "Running"),
        ("Cycling", "Cycling"),
        ("Weightlifting", "Weightlifting"),
        ("Swimming", "Swimming"),
        ("Walking", "Walking"),
        ("Other", "Other"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    duration = models.FloatField()  # in minutes
    distance = models.FloatField(blank=True, null=True)  # in km
    calories_burned = models.FloatField(blank=True, null=True)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.activity_type} - {self.user.username} on {self.date}"
