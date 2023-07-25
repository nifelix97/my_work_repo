from django.db import models
from django.urls import reverse

# Create your models here.
class event (models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    photo = models.ImageField(upload_to='speakers/', blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse("event_list")

    def __str__(self):
        return self.title