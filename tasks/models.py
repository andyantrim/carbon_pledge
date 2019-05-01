from django.db import models

# Create your models here.

class Tasks(models.Model):
    title = models.CharField(blank=False, null=False, max_length=256)
    decription = models.CharField(blank=True, null=True, max_length=5000)
    image_link = models.CharField(blank=False, null=False,
                                  default="http://www.worldwideprotective.com/Public/images/product/recycle.jpg",
                                  max_length=1024)

