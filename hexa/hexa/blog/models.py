from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, is_admin=False, is_active=True):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), is_active=is_active, is_admin=is_admin)
        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.full_clean()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class BaseUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email', unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"

    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
    posts_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)
    followers_count = models.PositiveIntegerField(default=0)
    bio = models.CharField(max_length=1000, null=True, blank=True)
