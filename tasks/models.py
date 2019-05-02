from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tasks(models.Model):
    title = models.CharField(blank=False, null=False, max_length=256)
    description = models.CharField(blank=True, null=True, max_length=5000)
    image_link = models.CharField(blank=False, null=False,
                                  default="http://www.worldwideprotective.com/Public/images/product/recycle.jpg",
                                  max_length=1024)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    active = models.BooleanField(default=False)
