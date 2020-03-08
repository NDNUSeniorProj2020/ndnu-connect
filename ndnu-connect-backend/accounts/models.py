import jwt

from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser):
    username = None
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'expt': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')


class Person(AbstractUser):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    graduated = models.IntegerField(null=True, blank=True)
    major = models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=20, null=True, blank=True)
    job_title = models.CharField(max_length=20, null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    '''
    def create_user(self, username, password):
        self.username=username
        self.password=password
        self.save()
        return self
    '''


    def __str__(self):
        return self.username
