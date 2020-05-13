from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
       user=models.OneToOneField(User,on_delete=models.DO_NOTHING)
       portfolio=models.URLField(blank=True)
       profile_pics=models.ImageField(upload_to='profile_pic',blank=True)

       def __str__ (self):
         return self.user.username
