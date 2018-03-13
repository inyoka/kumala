from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.CharField(max_length = 256, blank=True)
    site = models.URLField(blank=True)
    picture = models.ImageField(upload_to='picture', blank=True)

    def __str__(self):
        return f'{self.user.last_name}, {self.user.first_name}'
