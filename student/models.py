from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class studentacc(BaseUserManager):
    def create_user(self, Email, username,Department, password=None):
        if  not Email:
            raise ValueError('User must contain Email Address')
        if not username:
            raise ValueError('User must have Username')
        if not Department:
            raise ValueError('Department can''t be blank')
        if not password:
            raise ValueError('password can''t be blank')
        
        user= self.model(
            Email=self.normalize_email(Email),
            username=username,
            Department=Department,    
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Email, username, password=None):
        if  not Email:
            raise ValueError('User must contain Email Address')
        if not username:
            raise ValueError('User must have Username')

        user=self.model(
            Email=self.normalize_email(Email),
            username=username,
        )    
        
        user.set_password(password)
        user.is_admin=True
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user    


class Student(AbstractBaseUser, PermissionsMixin):
    choice=(
        ('CS', 'Computer Science'),
        ('EC', 'Electronics'),
        ('IS', 'Information Science'),
        ('TC', 'Telecommunication'),
        )

    Email        = models.EmailField(max_length=60, verbose_name='Email',unique=True)
    username     = models.CharField(max_length = 30, verbose_name='UserName', unique=True)
    datejoined   = models.DateTimeField(verbose_name='Date Joined',auto_now_add=True)
    Department   = models.CharField(max_length=10, choices=choice,)
    is_superuser = models.BooleanField(default=False)
    is_admin     = models.BooleanField(default=False)
    is_staff    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)

    USERNAME_FIELD ='username'
    REQUIRED_FIELDS= ['Email',]

    objects=studentacc()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



    