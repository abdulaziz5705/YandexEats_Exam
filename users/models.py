
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class UserRoleChoice(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    MANAGER = 'manager', 'Manager'
    COURIER = 'courier', 'Courier'
    User = 'user', 'User'


class UserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, role=UserRoleChoice.User, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, role=role, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser):
    first_name = models.CharField( max_length=100, blank=True, null=True)
    last_name = models.CharField( max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=50, choices=UserRoleChoice.choices, default=UserRoleChoice.User)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} ({self.get_role_display()})"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'



class VerificationModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='verification')
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email} - {self.code}'

    class Meta:
        verbose_name = 'Verification'
        verbose_name_plural = 'Verifications'
        unique_together = ('user', 'code')
