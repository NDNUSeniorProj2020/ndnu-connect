import jwt

from datetime import datetime, timedelta

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    objects = UserManager()

    def create(self, email, password):
        self.objects.create_user(email, password)
        return self

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'expt': int(dt.strftime('%S'))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    graduated = models.BooleanField(default=False)
    year_graduated = models.IntegerField(null=True, blank=True)
    major = models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=20, null=True, blank=True)
    job_title = models.CharField(max_length=20, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    first_name = models.TextField(default='accounts.User.get_first_name')
    last_name = models.TextField(default='accounts.User.get_last_name')

    def create(self, user, graduated, year_graduated, major, company, job_title, about):
        self.user = user
        self.graduated = graduated
        self.year_graduated = year_graduated
        self.major = major
        self.company = company
        self.job_title = job_title
        self.about = about

        self.save()
        return self

    def __str__(self):
        return self.user.email
