from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    special_user=models.DateTimeField(default=timezone.now,verbose_name='کاربر ویژه تا')
    profile_pic=models.ImageField(null=True,blank=True,upload_to='image',default='f.jpg',verbose_name='عکس پروفایل')
    email=models.EmailField(unique=True,verbose_name='ایمیل')
    def is_special_user(self):
        if self.special_user >timezone.now():
            return True
        else:
            return False
    is_special_user.boolean=True
    is_special_user.short_description='کاربر ویژه'



