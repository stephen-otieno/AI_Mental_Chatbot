from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50, unique=True)
    user_password1 = models.CharField(max_length=50)
    user_password2 = models.CharField(max_length=50)

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['user_name', 'user_password1', 'user_password2']

    def __str__(self):
        return self.user_name




# Create your models here.
