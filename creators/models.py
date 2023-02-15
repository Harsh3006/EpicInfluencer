from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
    )

class UserManager(BaseUserManager):
    def create_user(self, email, country, dob, password=None, is_staff=False, is_admin=False, is_active=True, is_email_verified=False):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a pasword')
        user = self.model(
            email = self.normalize_email(email),
            dob = dob,
            country = country
        )
        user.set_password(password)  #encoding the password
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.is_email_verified = is_email_verified
        user.save(using=self._db)
        return user

    def create_staffuser(self, dob, country, email, password=None):
        user = self.create_user(
            email, 
            password=password,
            is_staff = True,
            is_email_verified = True
            )
        return user

    def create_superuser(self, dob, country, email, password=None):
        user = self.create_user(
            email, 
            dob = dob,
            country = country,
            password=password,
            is_staff = True,
            is_admin = True,
            is_email_verified = True
            )
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    dob = models.DateField(verbose_name='Date of birth')
    country = models.CharField(max_length=50)
    is_email_verified = models.BooleanField(default=False)
    active = models.BooleanField(default=True)   #can login
    staff = models.BooleanField(default=False)   #staff user non-superuser
    admin = models.BooleanField(default=False)   #superuser
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    #email and password are required by default
    REQUIRED_FIELDS = ['dob', 'country'] 

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active