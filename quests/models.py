

# from enum import auto
# from tkinter.messagebox import QUESTION
from django.db import models
from django.urls import reverse 
from django.utils import timezone
from django.contrib.auth.models import User


class que(models.Model):
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=20)




    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class res(models.Model):
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    




    def __str__(self):
        return self.content

        
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})