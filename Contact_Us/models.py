from django.db import models

# Create your models here.
class contact(models.Model):
        fullname = models.CharField(max_length=200)
        email = models.EmailField()
        message = models.TextField()
        def __str__(self):
                return self.fullname