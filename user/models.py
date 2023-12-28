from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length= 30)
    city = models.CharField(max_length = 50, blank = True, null =True)
    phone = models.CharField(max_length = 11, blank = True, null = True)

    def __str__(self):
        return self.name

