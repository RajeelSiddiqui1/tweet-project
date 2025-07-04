from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserTweets(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f'{self.name.username} - {self.text}'
    
