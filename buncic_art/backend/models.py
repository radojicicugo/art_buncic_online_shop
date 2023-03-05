from django.db import models
from django.utils import timezone

# Create your models here.
class BackendArt(models.Model):
    upload_art = models.ImageField(upload_to='uploads/images',blank=False, null=False )
    title = models.CharField(max_length=250, unique=True)
    author = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
  
    def __str__(self):
        return self.title
