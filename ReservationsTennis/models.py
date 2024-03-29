from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,  related_name='Tennis_userprofile')
    selected_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
