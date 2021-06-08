from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    #Create relationship (dont inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #add any additional attributes
    portfolio_site = models.URLField(blank=True)
    #pip install pillow to use this!
    # Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg":
    profile_pic = models.ImageField(upload_to='basic_app/profile_pics', blank=True)

    def __str__(self):
        # built in attribute of django.contrib.auth.models.User
        return self.user.username
