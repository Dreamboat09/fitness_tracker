from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Profile(models.Model):
    sex=[
        ('MALE', 'male'),
        ('FEMALE', 'female')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30,)
    sex = models.CharField(max_length=6, choices=sex, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)  # in kilograms
    height = models.FloatField(null=True, blank=True)  # in centimeters
    fitness_goals = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.firstname}'s profile"
    

class Workout(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='workouts')
    date = models.DateField()
    calories_burned = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"workout on {self.date} for {self.profile.firstname}"
    

class Exercise(models.Model):
    levels = [
        ('EASY', 'easy'),
        ('MEDIUM', 'medium'),
        ('HARD', 'hard'),
    ]
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    activity_type = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    difficulty_level = models.CharField(max_length=6, choices=levels, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)  # in kilograms
    distance = models.FloatField(null=True, blank=True)  # in kilometers

    def __str__(self):
        return f"{self.activity_type} in workout on {self.workout.date}"