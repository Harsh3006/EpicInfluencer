from django.db import models
from creators.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Personal_Detail(models.Model):
    email = models.OneToOneField(User, verbose_name="Email Id", on_delete=models.CASCADE)
    fname = models.CharField(max_length=20, null=True, default=None)
    lname = models.CharField(max_length=30, null=True, default=None)
    gender = models.CharField(max_length=1, null=True, default=None)
    language = models.CharField(max_length=20, null=True, default=None)
    phoneNumber = PhoneNumberField(unique=True, null=True, default=None)
    address = models.TextField(null=True, default=None)
    address2 = models.TextField(null=True, default=None, blank=True)
    postalCode = models.CharField(max_length=6, null=True, default=None)
    city = models.CharField(max_length=100, null=True, default=None)
    state = models.CharField(max_length=50, null=True, default=None)
    department = models.CharField(max_length=50, null=True, default=None)

    def __str__(self):
        return (self.fname + ' ' + self.lname)

    
