from django.db import models
from django.conf import settings


#https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#auth-custom-user
#https://docs.djangoproject.com/en/3.2/topics/auth/customizing/
#https://docs.djangoproject.com/en/3.2/ref/settings/
#https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#django.contrib.auth.get_user_model

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile username {self.user.username}'

# Create your models here.
