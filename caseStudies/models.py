from django.db import models

# Create your models here.
class case_studies(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    product = models.CharField(max_length=15, blank=True)
    industry = models.CharField(max_length=20, blank=True)
    img = models.ImageField(upload_to='Images')
    brand = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    summary = models.TextField()
    
    def __str__(self):
        return self.brand