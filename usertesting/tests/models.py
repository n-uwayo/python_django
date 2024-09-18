from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class UserTesting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to Django's built-in User model
    task = models.ForeignKey(Task, on_delete=models.CASCADE)  # Link to the Task model
    feedback = models.TextField(blank=True)  # User's feedback after testing the task
    test_date = models.DateTimeField(auto_now_add=True)  # The date and time of testing
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=3)  # Rating from 1 to 5
    bugs_found = models.TextField(blank=True, null=True)  # Any bugs the user found

    def __str__(self):
        return f"Test by {self.user.username} on {self.test_date}"

