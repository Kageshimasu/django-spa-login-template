from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have a email address')
        email = CustomUserManager.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=128, unique=True)
    access_datetime = models.DateTimeField()
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user'
        swappable = 'AUTH_USER_MODEL'
