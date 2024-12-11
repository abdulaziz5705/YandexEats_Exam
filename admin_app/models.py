from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models

class ManagerandCourierModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    ROLE_CHOICES = (
        ('manager', 'Restaurant Manager'),
        ('courier', 'Courier'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')

    class Meta:
        verbose_name = 'Manager_and_Courier'
        verbose_name_plural = 'Manager_and_Couriers'
        db_table = 'manager_and_courier'

#
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.db import models
#
# class ManagerandCourierManager(BaseUserManager):
#     def create_user(self, email, username, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username, **extra_fields)
#         user.set_password(password)  # Hashes the password
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_staff', True)
#
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError("Superuser must have is_superuser=True.")
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#
#         return self.create_user(email, username, password, **extra_fields)
#
#
# class ManagerandCourierModel(AbstractBaseUser):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=50, unique=True)
#     ROLE_CHOICES = (
#         ('manager', 'Restaurant Manager'),
#         ('courier', 'Courier'),
#     )
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='courier')
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     objects = ManagerandCourierManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#
#     def __str__(self):
#         return self.email
