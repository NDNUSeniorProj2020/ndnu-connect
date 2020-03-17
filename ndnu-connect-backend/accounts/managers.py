from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, display_name, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address.')
        if password is None:
            raise ValueError('Users must have a valid password.')

        user = self.model(
            email=self.normalize_email(email),
            display_name=display_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, display_name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, display_name, **extra_fields)
